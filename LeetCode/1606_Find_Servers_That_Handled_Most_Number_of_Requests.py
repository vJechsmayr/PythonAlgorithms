class Solution(object):
    def busiestServers(self, k, arrival, load):
        """
        :type k: int
        :type arrival: List[int]
        :type load: List[int]
        :rtype: List[int]
        """
        from sortedcontainers import SortedList
        avail = SortedList()    
        for i in range(k):
            avail.add(i)
        h = []
        count = [0]*k 
        for i in range(len(arrival)):
            s = arrival[i]
            e = arrival[i]+load[i]
            while h and h[0][0]<=s:    
                _, j = heappop(h)
                avail.add(j)
            if len(h)==k:
                continue
            si = avail.bisect_left(i%k)
            if si==len(avail):
                ser = avail[0]
            else:
                ser = avail[si]         
            avail.remove(ser)               
            count[ser]+=1
            heappush(h, (e, ser))
        maxReq = max(count)
        ans = []
        for i in range(len(count)):
            if count[i]==maxReq:
                ans.append(i)
        return ans                                                                                                                                                                                                                                                                                                                                                                                                                                                    
