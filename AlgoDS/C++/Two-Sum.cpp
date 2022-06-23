#include <iostream>
#include <vector>
#include <map>

using namespace std;

vector<int> solve(vector<int> arr, int target) 
{
    map<int, int> visited;

    for (size_t i = 0; i < arr.size(); i++)
    {
        visited.insert(pair<int,int>(target-arr[i], arr[i]));
    }

    for (size_t i = 0; i < arr.size(); i++) 
    {
        if (visited.find(arr[i]) != visited.end()) {
            return vector<int>{arr[i], visited.find(arr[i])->second};
        }
    }

    return vector<int>{};
}
