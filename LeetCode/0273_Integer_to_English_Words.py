class Solution(object):
    def numberToWords(self, num: int) -> str:
        def decode(triple_str):
            final_list = []

            numbers = { "1": "One",
                        "2": "Two",
                        "3": "Three",
                        "4": "Four",
                        "5": "Five",
                        "6": "Six",
                        "7": "Seven",
                        "8": "Eight",
                        "9": "Nine",
                        "10": "Ten",
                        "11": "Eleven",
                        "12": "Twelve",
                        "13": "Thirteen",
                        "14": "Fourteen",
                        "15": "Fifteen",
                        "16": "Sixteen",
                        "17": "Seventeen",
                        "18": "Eighteen",
                        "19": "Nineteen"}

            tens    = { "2": "Twenty",
                        "3": "Thirty",
                        "4": "Forty",
                        "5": "Fifty",
                        "6": "Sixty",
                        "7": "Seventy",
                        "8": "Eighty",
                        "9": "Ninety"}

            if int(triple_str[0]) != 0:
                final_list.append("{} Hundred".format(numbers[triple_str[0]]))
            if int(triple_str[1]) == 1:
                final_list.append("{}".format(numbers[triple_str[1:3]]))
            else:
                if int(triple_str[1]) != 0:
                    final_list.append("{}".format(tens[triple_str[1]]))
                if int(triple_str[2]) != 0:
                    final_list.append("{}".format(numbers[triple_str[2]]))

            return final_list


        num_str = "{:0>12}".format(str(num))
        num_list = []
        final_num = ""
        digit_dict = {  0: "Billion",
                        3: "Million",
                        6: "Thousand"}

        for x in range(0, 12, 3):
            the_triple = num_str[x:x+3]
            if the_triple == "000":
                continue
            else:
                num_list.extend(decode(the_triple))
                if x == 9: break
                num_list.append(digit_dict[x])

        final_num = " ".join(num_list)
        if final_num == "":
            final_num = "Zero"

        return final_num
