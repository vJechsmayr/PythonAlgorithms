class Solution:
    def bitwiseComplement(self, N: int):

        flipped = ""


        while N > 0:
            # Getting the individual bit
            bit = N % 2
            flipped +=str(bit)

            # Factoring it out of N
            N = int(N / 2)

        # Complement is where each bit is flipped (eg 1 becomes 0 and vice versa)
        complement = ""
        for x in range(len(flipped)):

            # Checking each element from the end to the front and flipping
            current = flipped[len(flipped) - 1 - x]
            if current == "0":
                complement += "1"
            else:
                complement += "0"

        base_10 = 0
        for x in range(len(complement)):
            # Multiplying the bit by 2^x to convert to base 10
            current = complement[len(complement) - 1 - x]
            base_10 += (2 ** x) * int(current)
        return base_10
