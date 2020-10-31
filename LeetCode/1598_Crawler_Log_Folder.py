class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for log in logs:
            if log == "../":
                if cnt != 0:
                    cnt -= 1
                continue
            elif log == "./":
                continue
            else:
                cnt += 1
        return cnt if cnt > 0 else 0
