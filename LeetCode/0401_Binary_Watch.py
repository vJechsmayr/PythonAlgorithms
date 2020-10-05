class Solution:
    def readBinaryWatch(self, num: int):
        result = []
        for hours in range(12):
            for minutes in range(60):
                if bin(hours).count('1') + bin(minutes).count('1') == num:
                    result.append(str(hours) + ":" + str(minutes).zfill(2))
        return result