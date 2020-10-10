'''
337. House Robber III
The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.
Example 1:
            Input: [3,2,3,null,3,null,1]
                 3
                / \
               2   3
                \   \ 
                 3   1

Output: 7 
            Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Time Complexity:- O(N) 
Space Complexity:- O(N), as we are using dictionary to memoize the solution
'''

def rob(self, root: TreeNode) -> int:
    # this dp dictionary will help us reduce the time complexity by memoizing the solutions
    dp = {}

    # this function will return the max profit that we can get 
    def rob_helper(root):
        # base cases
        if(root is None):
            return 0
        # if we have the value for root in dp that we means we have calculated the value
        # previously so we can simply return the saved value
        if(root in dp.keys()):
            return dp[root]
        '''
        In this problem our constraints are:-
            1. If we add/rob the profit of parent then we can't add/rob profit of children
               as the police will be alerted
            2. If we don't rob the parent then we can rob its child nodes 
             
             Example:-

            lvl 1            3
                            / \
            lvl 2          2   3
                            \   \ 
            lvl 3            3   1
            In this if we add the profit for 3 then we can't add 2 and 3 from level 2 but add 3 and 1 from level 3
            If we add 2 and 3 from level 2 then we can't add profit from level 1 and 3
            Therefore, in a nutshell WE CAN'T ADD THE PROFIT OF 2 ADJACENT LEVEL/HOUSES

        '''

        # It is the total profit if we exclude the parent and add the left and right child
        profit1 = rob_helper(root.left) + rob_helper(root.right)

        # In this case we left child nodes and added the profit for parent node
        profit2 = root.val
        # As we robbed the parent node so we can't rob children
        #  but we can rob children of left and right child of parent

        # If root.left has left and right children then add there profit
        if(root.left is not None):
            profit2 += rob_helper(root.left.left) + rob_helper(root.left.right)
        # If root.right has left and right children then add there profit
        if(root.right is not None):
            profit2 += rob_helper(root.right.left) + rob_helper(root.right.right)

        # save the max value in DP to memoize the solution
        dp[root] = max(profit1, profit2)

        return dp[root]

    return rob_helper(root)
