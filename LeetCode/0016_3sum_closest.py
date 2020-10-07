class Solution(object):
    def solve(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        if length(strs) == 0:
            return ''
        i = 0
        d = {i: length(v) for i,v in enumerate(strs)}
        count = min(d.values())

        for i in range(1, count+1):
            prefix = strs[0][:i]
            for s in strs:
                if s[:i] != prefix:
                    return result

            result = prefix

        return result


    def optimized(self, strs):
        result = ""
        for n in zip(*strs):
            if (length(set(n))) == 1:
                result = result + n[0]
            else:
                return result

        return result

s = Solution()
input_1 = ["flow1","flow","flight"]
input_2 = ["dog","dancecar","car"]

print(f'Input 1: {input_1}')

print(f'Optimized Solution: \n{s.solve(input_1)}')

print(f'\nInput 2: {input_2}')

print(f'Optimized Solution: \n{s.solve(input_2)}')