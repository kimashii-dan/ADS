#include <iostream>
#include <vector>

using namespace std;

int find_block(const vector<int>& ranges, int b, int N) {
    int left = 0, right = N - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (ranges[mid] >= b) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return left + 1;
}

int main() {
    int N, M;
    cin >> N >> M;
    
    vector<int> a(N);
    vector<int> ranges(N);

    cin >> a[0];
    ranges[0] = a[0];
    for (int i = 1; i < N; ++i) {
        cin >> a[i];
        ranges[i] = ranges[i - 1] + a[i];
    }

    vector <int> results;

    for (int i = 0; i < M; ++i) {
        int b;
        cin >> b;

        int block = find_block(ranges, b, N);
        
        results.push_back(block)
    }

    for (int block: results){
        cout << block;
    }
}
