class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen_emails = set()
        for item in emails:
            name, domain = item.split('@')
            special_index = name.find('+')
            if special_index != -1:
                name = name[: special_index]
            seen_emails.add(name.replace('.', '') + '@' + domain)
        return len(seen_emails)
        