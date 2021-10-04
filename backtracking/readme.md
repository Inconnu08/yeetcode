# **Backtracking**
<hr>

### **Subsets**

A set is a list of elements where order and repetition does not matter.<br>
A subset is a set that contains any elements (not all) that exist within the original parent set. <br>
A power set is the set of all subsets for any given set, including the empty set. There are 2^n subsets in the power set. 
To find all these subsets, we have to basically choose or not choose the current element, for n numbers of elements provided, hence it's 2^n.
This can be done recursively, more specifically backtracking.  

Here cur represents our current subset while we use it build up the complete solution. 
The first thing we'll do in our backtracking function is at whatever iteration we are on, we add that to our powerset list. We thing to notice here with cur is that we are deep copying the cur list since we will keep modifying our cur list.
Now we need to walk through all the remaining numbers and branch out by deciding choosing and not choosing that current number where on. We will now walk through all the numbers in the list. To do this, will use a for loop that starts with the current index and walk all the way to the end of the nums list. So in our loop for first choose and take that number into our current solution space and then proceed to the next element in the nums list by recursively calling our function with the next index. Finally when we return from this function, we remove the last added num from our cur list, this works as a not choosing a number part. Like choose the current number, not choose the current number. 

Time complexity: O(n*2^n) - running time is 2^n where n is the number of elements in the num list. Since we are making 2 choices(choose and not choose current num) meaning two recursive calls for every iteration. That times n for the loop.

Space complexity: O(n) since its recursive and we are going n levels deep in the call stack.

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


