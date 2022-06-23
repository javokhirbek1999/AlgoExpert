/*
Time: O(n^2)
Space: O(1)
*/

#include <iostream>
#include <vector>
#include <string>


using namespace std;

vector<int> getLongestPalindrome(int leftIndex, int rightIndex, string s);
vector<int> getMax(vector<int> a, vector<int> b);

string longestPalindrome(string s)
{
    vector<int> currentLongest = {0,1};

    for (int i = 1; i<s.size(); i++)
    {
        vector<int> odd = getLongestPalindrome(i-1, i+1, s);
        vector<int> even = getLongestPalindrome(i-1, i, s);

        auto longest = getMax(odd, even);
        currentLongest = getMax(currentLongest, longest);

    }

    string res = "";

    for (int i = currentLongest[0]; i<currentLongest[1]; i++) 
    {
        res+=s[i];
    }

    return res;

}

vector<int> getLongestPalindrome(int leftIndex, int rightIndex, string s)
{
    while (leftIndex > 0 && rightIndex < s.size())
    {
        if (s[leftIndex] != s[rightIndex]) {
            break;
        }

        leftIndex--;
        rightIndex++;
    }

    return vector<int>{leftIndex+1, rightIndex};
}

vector<int> getMax(vector<int> a, vector<int> b) 
{
    int a_res = a[1]-a[0];
    int b_res = b[1]-b[0];

    return a_res > b_res ? a : b;
}
