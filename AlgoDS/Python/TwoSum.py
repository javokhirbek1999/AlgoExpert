"""
Approach #1

Time: O(n)
Space: O(n)
"""

def solve(arr: list, target: int) -> list:

    visited = {}

    for current in arr:
        temp = target-current

        if temp in visited:
            return [temp, current]
        
        visited[current] = True

    return []





"""
Approach #2

Time: O(n)
Space: O(n)
"""

def solve(arr: list, target: int) -> list:
    

    visited = {}

    for current in arr:
        visited[target-current] = current
    
    for current in arr:
        if current in visited:
            return [visited[current], current]
    
    return []



"""
Approach #3: Two pointers

Time: O(n log n)
Space: O(1)
"""

def solve(arr: list, target: int) -> list:

    arr.sort() # O(n log n)

    left, right = 0, len(arr)-1

    while left != right:

        currentSum = arr[left]+arr[right]

        if currentSum == target:
            return [arr[left], arr[right]]
        
        if currentSum < target:
            left += 1
        else:
            right -= 1

    return []
