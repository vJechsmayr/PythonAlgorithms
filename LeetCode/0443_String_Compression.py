class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        while read < len(chars) - 1:
            count = 1
            read_next = read + 1
            while read < len(chars) - 1 and chars[read_next] == chars[read]:
                del chars[read_next]
                count += 1
            if count > 1:
                for char in str(count):
                    chars.insert(read_next, char)
                    read_next += 1
            read = read_next
        return len(chars)
    
