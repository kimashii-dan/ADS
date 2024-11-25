#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int countInRange(const vector<int>& a, int l, int r) {
    int left = 0, right = a.size() - 1;
    int start = -1, end = -1;

    while (left <= right) {
        int mid = (left + right) / 2;
        if (a[mid] >= l) {
            start = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    left = 0;
    right = a.size() - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        if (a[mid] <= r) {
            end = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    if (start == -1 || end == -1 || start > end)
        return 0;
    return end - start + 1;
}

int main() {
    int n, q;
    cin >> n >> q;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    while (q--) {
        int l1, r1, l2, r2;
        cin >> l1 >> r1 >> l2 >> r2;
        int countRange1 = countInRange(a, l1, r1);
        int countRange2 = countInRange(a, l2, r2);
        int countCommon = countInRange(a, max(l1, l2), min(r1, r2));
        int total = countRange1 + countRange2 - countCommon;
        cout << total << endl;
    }

    return 0;
}
