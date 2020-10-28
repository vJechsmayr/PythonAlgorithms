class Solution(object):
        def minOperationsMaxProfit(self, customers, boardingCost, runningCost) :
            """
            :type customers: List[int]
            :type boardingCose: int
            :type runningCose: int
            :rtype: int
            """
            wait = 0
            pro = 0                                                             
            high = 0
            res = -1
            for i in range(len(customers)):
                vacc = 4 - wait
                if vacc <= 0:
                    wait += customers[i] - 4
                    pro += 4 * boardingCost - runningCost
                # board all
                elif customers[i] <= vacc: # board=customers[i]+wait
                    pro += boardingCost * (customers[i] + wait) - runningCost
                    wait = 0
                else:
                    pro += boardingCost * 4 - runningCost
                    wait += customers[i] - 4
                if pro > high:
                    high = pro
                    res = i
            # determine after all arrives
            pro_per = boardingCost * 4 - runningCost
            if pro_per > 0:
                last = wait % 4
                if wait >= 4:
                    if boardingCost * last - runningCost > 0: 
                        return len(customers) + wait // 4 + 1
                    else: 
                        return len(customers) + wait // 4
                if boardingCost * last - runningCost > 0: 
                    return len(customers) + 1
            return res + 1 if res >= 0 else -1
