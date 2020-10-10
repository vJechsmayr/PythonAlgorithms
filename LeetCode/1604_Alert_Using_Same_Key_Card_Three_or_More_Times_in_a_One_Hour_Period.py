class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        mapp = {}
        for i in range(len(keyName)):
            name = keyName[i]
            if(name not in mapp):
                mapp[name] = [keyTime[i]]
            else:
                mapp[name].append(keyTime[i])
        res = []
        for name, arr in mapp.items():
            arr.sort()
            for i in range(len(arr)-2):
                time= arr[i]
                t2 = arr[i+1]
                t3 = arr[i+2]
                if(time[0:2]=="23"):
                    endTime = "24:00"
                    if(t2<=endTime and t3<=endTime and t2>time and t3>time):
                        res.append(name)
                        break
                else:
                    start = int(time[0:2])
                    endTime = str(start+1)+time[2:]
                    if(start<9):
                        endTime = "0"+endTime
                    if(t2<=endTime and t3<=endTime):
                        res.append(name)
                        break
        return sorted(res)
