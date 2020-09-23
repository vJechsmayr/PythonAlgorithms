class Solution:
    values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    romanNumerals = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        
    def intToRoman(self, num: int, ptr: int = len(values) - 1) -> str:
        if num == 0:
            return ""
        
        while True:
            if num >= self.values[ptr]:                
                return self.romanNumerals[ptr] + self.intToRoman(num - self.values[ptr], ptr)
            else:
                ptr -= 1
