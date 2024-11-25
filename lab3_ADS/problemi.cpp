#include <iostream>
using namespace std;

int binary_search(int elements[], int n, int target) {
    int low = 0;
    int high = n - 1;
    while (low <= high) {
        int mid = (high + low) / 2;
        if (target == elements[mid]) {
            return mid;
        }
        if (target > elements[mid]) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}

int main() {
    int n, target;
    cin >> n;
    int elements[n];
    for (int i = 0; i < n; ++i) {
        cin >> elements[i];
    }

    cin >> target;

    if (binary_search(elements, n, target) != -1) {
        cout << "Yes";
    } else {
        cout << "No";
    }
}