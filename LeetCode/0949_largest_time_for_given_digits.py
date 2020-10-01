from collections import defaultdict


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        num_dict = defaultdict(lambda: 0)
        for i in arr:
            num_dict[i] += 1

        time_val = [0, 0, 0, 0]
        index = 0

        def item_filter(x):
            if num_dict[x] > 0:
                if index == 0:
                    if x <= 2:
                        return True
                    else:
                        return False
                elif index == 1:
                    if time_val[0] < 2:
                        return True
                    else:
                        if x <= 3:
                            return True
                        else:
                            return False
                elif index == 2:
                    if x <= 6:
                        return True
                    else:
                        return False
                else:
                    if time_val[2] < 6:
                        return True
                    else:
                        if x == 0:
                            return True
                        else:
                            return False
            else:
                return False

        for i in range(len(time_val)):
            index = i
            val_list = list(filter(item_filter, arr))
            if len(val_list) > 0:
                max_val = max(val_list)
                time_val[i] = max_val
                num_dict[max_val] -= 1
            else:
                return ""

        return str(time_val[0]) + str(time_val[1]) + ":" + str(time_val[2]) + str(time_val[3])
