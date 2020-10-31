import requests, os, re, json, time
from bs4 import BeautifulSoup
from github import Github
from dotenv import load_dotenv

load_dotenv()
#load_dotenv(dotenv_path='sample.env')

LC_BASE = 'https://leetcode.com'
LC_CSRF = LC_BASE + '/ensure_csrf/'
LC_LOGIN = LC_BASE + '/accounts/login/'
LC_GRAPHQL = LC_BASE + '/graphql'
LC_CATEGORY_PROBLEMS = LC_BASE + '/api/problems/{category}'
LC_PROBLEM = LC_BASE + '/problems/{slug}/description'
LC_TEST = LC_BASE + '/problems/{slug}/interpret_solution/'
LC_SUBMIT = LC_BASE + '/problems/{slug}/submit/'
LC_SUBMISSIONS = LC_BASE + '/api/submissions/{slug}'
LC_SUBMISSION = LC_BASE + '/submissions/detail/{submission}/'
LC_CHECK = LC_BASE + '/submissions/detail/{submission}/check/'
LC_PROBLEM_SET_ALL = LC_BASE + '/problemset/all/'
LC_PROGRESS_ALL = LC_BASE + '/api/progress/all/'

def _break_code_lines(s):
    return s.replace('\r\n', '\n').replace('\xa0', ' ').split('\n')

def _break_paragraph_lines(s):
    lines = _break_code_lines(s)
    result = []
    # reserve one and only one empty line between two non-empty lines
    for line in lines:
        if line.strip() != '':  # a line with only whitespaces is also empty
            result.append(line)
            result.append('')
    return result


def _remove_description(code):
    eod = code.find('[End of Description]')
    if eod == -1:
        return code
    eol = code.find('\n', eod)
    if eol == -1:
        return ''
    return code[eol+1:]

def _split(s):
    if isinstance(s, list):
        lines = []
        for element in s:
            lines.extend(_split(element))
        return lines

    # Replace all \r\n to \n and all \r (alone) to \n
    s = s.replace('\r\n', '\n').replace('\r', '\n').replace('\0', '\n')
    # str.split has an disadvantage that ''.split('\n') results in [''], but what we want
    # is []. This small function returns [] if `s` is a blank string, that is, containing no
    # characters other than whitespaces.
    if s.strip() == '':
        return []
    return s.split('\n')

def _make_headers():
    assert is_login()
    headers = {'Origin': LC_BASE,
               'Referer': LC_BASE,
               'X-Requested-With': 'XMLHttpRequest',
               'X-CSRFToken': session.cookies.get('csrftoken', '')}
    return headers

def get_progress():
    headers = _make_headers()
    res = session.get(LC_PROGRESS_ALL, headers=headers)
    if res.status_code != 200:
        _echoerr('cannot get the progress')
        return None

    data = res.json()
    if 'solvedTotal' not in data:
        return None
    return data

def _status_to_name(status):
    if status == 10:
        return 'Accepted'
    if status == 11:
        return 'Wrong Answer'
    if status == 12:
        return 'Memory Limit Exceeded'
    if status == 13:
        return 'Output Limit Exceeded'
    if status == 14:
        return 'Time Limit Exceeded'
    if status == 15:
        return 'Runtime Error'
    if status == 16:
        return 'Internal Error'
    if status == 20:
        return 'Compile Error'
    if status == 21:
        return 'Unknown Error'
    return 'Unknown State'


def load_session_cookie(leetSession):
    my_cookie = {
        "version": 0,
        "name": 'LEETCODE_SESSION',
        "value": leetSession,
        "port": None,
        #"port_specified":False,
        "domain": '.leetcode.com',
        #"domain_specified":False,
        #"domain_initial_dot":True,
        "path": '/',
        # "path_specified":True,
        "secure": 1,
        "expires": None,
        "discard": True,
        "comment": None,
        "comment_url": None,
        "rest": {},
        "rfc2109": False
    }

    session_cookie = my_cookie
    #session_cookie_raw = pickle.dumps(**my_cookie, protocol=0).decode('utf-8')
    global session
    session = requests.Session()
    session.cookies.set(**session_cookie)

    progress = get_progress()
    if progress is None:
        keyring.delete_password('leetcode', 'SESSION_COOKIE')
        return False

    return True

def _check_result(submission_id):

    while True:
        headers = _make_headers()
        url = LC_CHECK.format(submission=submission_id)
        res = session.get(url, headers=headers)
        if res.status_code != 200:
            _echoerr('cannot get the execution result')
            return None

        r = res.json()
        if r['state'] == 'SUCCESS':
            prog_stage = 'Done      '
            break
        elif r['state'] == 'PENDING':
            prog_stage = 'Pending   '
        elif r['state'] == 'STARTED':
            prog_stage = 'Running   '

        time.sleep(1)

    result = {
        'answer': r.get('code_answer', []),
        'runtime': r['status_runtime'],
        'state': _status_to_name(r['status_code']),
        'testcase': _split(r.get('input', r.get('last_testcase', ''))),
        'passed': r.get('total_correct') or 0,
        'total': r.get('total_testcases') or 0,
        'error': _split([v for k, v in r.items() if 'error' in k and v])
    }

    # the keys differs between the result of testing the code and submitting it
    # for submission judge_type is 'large', and for testing judge_type does not exist
    if r.get('judge_type') == 'large':
        result['answer'] = _split(r.get('code_output', ''))
        result['expected_answer'] = _split(r.get('expected_output', ''))
        result['stdout'] = _split(r.get('std_output', ''))
        result['runtime_percentile'] = r.get('runtime_percentile', '')
    else:
        # Test states cannot distinguish accepted answers from wrong answers.
        if result['state'] == 'Accepted':
            result['state'] = 'Finished'
        result['stdout'] = _split(r.get('code_output', []))
        result['expected_answer'] = []
        result['runtime_percentile'] = r.get('runtime_percentile', '')
        result['expected_answer'] = r.get('expected_code_answer', [])
    return result


def submit_solution(slug, filetype, code=None):
    assert is_login()
    problem = get_problem(slug)
    if not problem:
        return None

    code = _remove_description(code)

    headers = _make_headers()
    headers['Referer'] = LC_PROBLEM.format(slug=slug)
    body = {'data_input': problem['testcase'],
            'lang': filetype,
            'question_id': str(problem['id']),
            'test_mode': False,
            'typed_code': code,
            'judge_type': 'large'}
    url = LC_SUBMIT.format(slug=slug)

    res = session.post(url, json=body, headers=headers)

    if res.status_code != 200:
        if 'too fast' in res.text:
            print('you are sending the request too fast')
        else:
            print('cannot submit the solution for ' + slug)
        return None

    result = _check_result(res.json()['submission_id'])
    result['title'] = problem['title']
    return result

def is_login():
    return session and 'LEETCODE_SESSION' in session.cookies

def get_problem(slug):
    assert is_login()
    headers = _make_headers()
    headers['Referer'] = LC_PROBLEM.format(slug=slug)
    body = {'query': '''query getQuestionDetail($titleSlug : String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    content
    stats
    difficulty
    codeDefinition
    sampleTestCase
    enableRunCode
    translatedContent
  }
}''',
            'variables': {'titleSlug': slug},
            'operationName': 'getQuestionDetail'}
    res = session.post(LC_GRAPHQL, json=body, headers=headers)
    if res.status_code != 200:
        _echoerr('cannot get the problem: {}'.format(slug))
        return None

    q = res.json()['data']['question']
    content = q['translatedContent'] or q['content']
    if content is None:
        _echoerr('cannot get the problem: {}'.format(slug))
        return None

    soup = BeautifulSoup(content, features='html.parser')
    problem = {}
    problem['id'] = q['questionId']
    problem['fid'] = q['questionFrontendId']
    problem['title'] = q['title']
    problem['slug'] = slug
    problem['level'] = q['difficulty']
    problem['desc'] = _break_paragraph_lines(soup.get_text())
    problem['templates'] = {}
    for t in json.loads(q['codeDefinition']):
        problem['templates'][t['value']] = _break_code_lines(t['defaultCode'])
    problem['testable'] = q['enableRunCode']
    problem['testcase'] = _split(q['sampleTestCase'])
    stats = json.loads(q['stats'])
    problem['total_accepted'] = stats['totalAccepted']
    problem['total_submission'] = stats['totalSubmission']
    problem['ac_rate'] = stats['acRate']
    return problem



# load details from ENV
repo_name = os.getenv("REPO_NAME")
access_token = os.getenv("GITHUB_ACCESS_TOKEN")
pull_number = int(os.getenv("PR_NUMBER"))
leetcode_csrf_token = os.getenv("LEETCODE_CSRF_TOKEN")
leetcode_session_token = os.getenv("LEETCODE_SESSION_TOKEN")

# authentication
g = Github(access_token)
repo = g.get_repo(repo_name)

# get PR details
pull = repo.get_pull(pull_number)
all_files = pull.get_files()

# get details of files from PR
file_url = ""
problem_name = ""
for i in all_files:
    if i.filename[-3:] == ".py":
        file_url = i.raw_url
        problem_name = i.filename[9:].lower()

# parse question id and problem name
question_id = int(problem_name[0:4])
problem_name = re.sub("_", "-", problem_name[5:-3])

# get file code
r = requests.get(file_url)
code = r.text

load_session_cookie(leetcode_session_token)
result = submit_solution(problem_name,'python3',code)
if result is None:
    print("Nothing to do")
elif result['state'] == 'Finished':
    pull.create_issue_comment("All test case have been passed, can be merged")
else:
    pull.create_issue_comment(result['state'])
