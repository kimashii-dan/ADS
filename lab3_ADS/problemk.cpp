#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int minSubarrayLength(int n, int k, vector<int>& arr) {
    int minLength = INT_MAX;
    int windowSum = 0;
    int left = 0;

    for (int right = 0; right < n; ++right) {
        windowSum += arr[right];
        while (windowSum >= k) {
            minLength = min(minLength, right - left + 1);
            windowSum -= arr[left];
            ++left;
        }
    }

    return minLength;
}

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> arr(n);

    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
    }

    int result = minSubarrayLength(n, k, arr);
    cout << result << endl;

    return 0;
}
