class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        dict_email ={}
        for email in emails:
            correct_email = self.correct_email(email)
            if correct_email not in dict_email:
                dict_email[correct_email] = 1
            else:
                dict_email[correct_email] += 1
            
        return len(dict_email)
    
    def correct_email(self,email):
        local_name,domain = email.split('@')
        fix_name = ""
        for i in local_name:
            if i == '+':
                break
            elif i=='.':
                pass
            else:
                fix_name += i
        return fix_name+'@'+domain
