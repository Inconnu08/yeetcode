# **Backtracking**
<hr>

### **Subsets**

A set is a list of elements where order and repetition does not matter.<br>
A subset is a set that contains any elements (not all) that exist within the original parent set. <br>
A power set is the set of all subsets for any given set, including the empty set.

##### Subsets I

        def subsets(nums: List[int]) -> List[List[int]]:
        powerset = []
        
        def backtrack(start, subset):
            powerset.append(subset.copy())
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        backtrack(0, [])
        return powerset

##### Subsets II (_with duplicates_)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        powerset = []
        
        def backtrack(start, subset):
            powerset.append(subset.copy())
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        
        backtrack(0, [])
        return powerset  

##### Permutations
    def permute(nums: List[int]) -> List[List[int]]:
        permutations = []
        
        def backtrack(cur):
            if len(cur) == len(nums): # bounding function
                permutations.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in cur:
                    continue
                cur.append(nums[i])
                backtrack(cur)
                cur.pop()
            
        backtrack([])
        return permutations
##### Permutations II (_with duplicates_)
    def permuteUnique(nums: List[int]) -> List[List[int]]:
        nums.sort()
        permutations, visited = [], [False] * len(nums)
        
        def backtrack(cur):
            if len(cur) == len(nums):
                permutations.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if visited[i] or i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                visited[i] = True
                cur.append(nums[i])
                backtrack(cur)
                visited[i] = False
                cur.pop()
        
        backtrack([])
        return permutations


