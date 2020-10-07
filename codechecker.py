import requests, os, re, json
from github import Github

from dotenv import load_dotenv

load_dotenv(dotenv_path='sample.env')

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
        problem_name = i.filename.lower()

# parse question id and problem name
question_id = int(problem_name[0:4])
problem_name = re.sub("_", "-", problem_name[5:-3])

# get file code
r = requests.get(file_url)
code = r.text

# craft request
leetcode_submission_url = f"https://leetcode.com/problems/{problem_name}/submit/"
language = "python3"
headers = {
    "Origin": "https://leetcode.com",
    "content-type": "application/json",
    "X-CSRFToken": leetcode_csrf_token,
    "Referer": leetcode_submission_url,
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0",
    # "Cookie": f"csrftoken={leetcode_csrf_token};LEETCODE_SESSION={leetcode_session_token}",
}
cookies = {
    "csrftoken": leetcode_csrf_token,
    "LEETCODE_SESSION": leetcode_session_token,
}
body = {"question_id": str(question_id), "lang": language, "typed_code": code}

# send request
submit = requests.post(
    leetcode_submission_url, headers=headers, data=body, cookies=cookies
)

print(submit.status_code)

# get from submit url response
submission_id = ""

# check submission against submission_id
leetcode_checker_url = f"https://leetcode.com/submissions/detail/{submission_id}/check/"


# sample request body extracted from network tab: {"question_id":"231","lang":"python3","typed_code":"class Solution:\n    def isPowerOfTwo(self, x: int) -> bool:\n        return (x != 0) and ((x & (x - 1)) == 0); \n"}
# get status of submission