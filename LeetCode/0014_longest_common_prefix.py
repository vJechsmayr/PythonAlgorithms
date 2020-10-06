class Solution(object):
    def bruteforce(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ''
        if len(strs) == 0:
            return ''
        i = 0
        d = {i: len(v) for i,v in enumerate(strs)}
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
            if (len(set(n))) == 1:
                result = result + n[0]
            else:
                return result

        return result

s = Solution()
input_1 = ["flower","flow","flight"]
input_2 = ["dog","racecar","car"]

print(f'Input 1: {input_1}')
print(f'Bruteforce Solution: \n{s.bruteforce(input_1)}')
print(f'Optimized Solution: \n{s.bruteforce(input_1)}')

print(f'\nInput 2: {input_2}')
print(f'Bruteforce Solution: \n{s.bruteforce(input_2)}')
print(f'Optimized Solution: \n{s.bruteforce(input_2)}')
