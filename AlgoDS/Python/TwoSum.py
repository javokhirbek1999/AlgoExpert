"""
Approach #1
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
"""

def solve(arr: list, target: int) -> list:
    

    visited = {}

    for current in arr:
        visited[target-current] = current
    
    for current in arr:
        if current in visited:
            return [visited[current], current]
    
    return []
