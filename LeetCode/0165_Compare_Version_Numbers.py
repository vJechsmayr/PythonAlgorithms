class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        while len(v1) < len(v2):
            v1.append("0")
        while len(v2) < len(v1):
            v2.append("0")
        for i in range(len(v1)):
            a = int(v1[i])
            b = int(v2[i])
            if a != b:
                return (a-b)//abs(a-b)
        return 0
