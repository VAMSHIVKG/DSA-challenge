# # print pattern [1],[2,2],[3,3,3]
# n=5
# t=[[i]*i for i in range(1,n+1)]
# for row in t:
#     print(row)

# for row in t:
#     print(*row)

# # continue the sum until we get single digit without using loop

# print('/n')

# # continue the iteration 

# a=[1,2,3,4,5]
# while(1): #0-->1
#     for i in range(len(a)):
#         print(a[i],end=' ')

#path sum 3
class TreeNode:
    def __init__(self,d):
        self.right = None
        self.left = None
        self.d = d

def pathsum3(root,targetsum):
    def dfs(root,curr_sum):
        nonlocal count
        curr_sum += root.d
        if curr_sum == targetsum:
            count+=1

        dfs(root.right,curr_sum)
        dfs(root.left,curr_sum)
        
    count=0
    dfs(root,0)
    return count

#driver code
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
# root.right.left = TreeNode(13)
root.right.right = TreeNode(11)
# root.right.right.left = TreeNode(5)
# root.right.right.right = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)
pathsum3(root,8)