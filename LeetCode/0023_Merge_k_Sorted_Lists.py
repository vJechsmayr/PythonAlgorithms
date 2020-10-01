class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        output = {}
        for node in lists:
            cur = node
            while cur:
                if cur.val not in output:
                    output[cur.val] = [cur, cur]
                else:
                    output[cur.val][1].next = cur
                    output[cur.val][1] = cur
                cur = cur.next
        sorted_keys = sorted(list(output.keys()))

        for k in range(len(sorted_keys) - 1):
            output[sorted_keys[k]][1].next = output[sorted_keys[k + 1]][0]
        if sorted_keys:
            return output[sorted_keys[0]][0]
        else:
            return None
