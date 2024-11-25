#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, f;
vector<int> c;

bool canDeliver(int bagCapacity) {
    int flightsNeeded = 0;
    for (int i = 0; i < n; i++) {
        flightsNeeded += (c[i] + bagCapacity - 1) / bagCapacity;
        if (flightsNeeded > f) {
            return false;
        }
    }
    return flightsNeeded <= f;
}

int findCapacity() {
    int left = 1;
    int right = *max_element(c.begin(), c.end());

    while (left < right) {
        int mid = (left + right) / 2;
        if (canDeliver(mid)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}

int main() {
    cin >> n >> f;
    c.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> c[i];
    }

    cout << findCapacity() << endl;
    return 0;
}