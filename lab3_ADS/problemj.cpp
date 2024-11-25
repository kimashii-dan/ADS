#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool canSteal(vector<int>& bags, int h, int K) {
    int totalhours = 0;
    for (int bars : bags) {
        totalhours += (bars + K - 1) / K;
        if (totalhours > h) {
            return false;
        }
    }
    return true;
}

int findK(vector<int>& bags, int h) {
    int low = 1, high = *max_element(bags.begin(), bags.end());
    int result = high;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (canSteal(bags, h, mid)) {
            result = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    return result;
}

int main() {
    int n, h;
    cin >> n >> h;
    vector<int> bags(n);
    for (int i = 0; i < n; ++i) {
        cin >> bags[i];
    }
    
    int minK = findK(bags, h);
    cout << minK << endl;
    
    return 0;
}
