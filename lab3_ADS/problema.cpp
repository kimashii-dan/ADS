#include <iostream>
using namespace std;

int binarySearch(int arr[], int m, int target, bool isDesc) {
    int low = 0;
    int high = m - 1;
    while (low <= high) {
        int mid = (low + high) / 2;
        if (arr[mid] == target)
            return mid;
        
        if (isDesc) {
            if (arr[mid] > target)
                low = mid + 1;
            else
                high = mid - 1;
        } else {
            if (arr[mid] < target)
                low = mid + 1;
            else
                high = mid - 1;
        }
    }
    
    return -1;
}

int main() {
    
    int t;
    cin >> t;
    int elements[t];
    for (int i = 0; i < t; ++i)
        cin >> elements[i];

    int n, m;
    cin >> n >> m;
    int snake[n][m];
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> snake[i][j];
        }
    }

    for (int i = 0; i < t; ++i) {
        int target = elements[i];
        for (int row = 0; row < n; ++row) {
            bool isDesc = (row % 2 == 0);
            int col = binarySearch(snake[row], m, target, isDesc);
            if (col != -1) {
                cout << row << " " << col << endl;
                break;
            }
            if (row == n - 1 && col == -1) {
                cout << -1 << endl;
            }
        }
    }
}