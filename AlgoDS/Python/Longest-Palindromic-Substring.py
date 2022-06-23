"""
Time: O(n^2)
Space: O(1)
"""
def longestPalindrome(string):
    
    currentLongest = [0, 1]

    for i in range(1, len(string)):
        odd = getLongestPalindrome(i-1, i+1, string)
        even = getLongestPalindrome(i-1, i, string)

        longest = max(odd, even, key=lambda x:x[1] - x[0])

        currentLongest = max(currentLongest, longest, key=lambda x:x[1] - x[0])
    
    start, end = currentLongest

    return string[start:end]
    

def getLongestPalindrome(leftIndex, rightIndex, string):
    
    while leftIndex >= 0 and rightIndex < len(string):

        if string[leftIndex] != string[rightIndex]:
            break

        leftIndex -= 1
        rightIndex += 1

    return [leftIndex+1, rightIndex]


print(longestPalindrome("axyztzyxb"))
