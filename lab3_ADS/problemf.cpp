#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int binary_search(const vector<int>& competitors, int markPower) {
    int low = 0, high = competitors.size() - 1;
    while (low <= high) {
        int mid = low + high / 2;
        if (competitors[mid] <= markPower)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return low;
}

int main() {
    int N, P;
    cin >> N;
    
    vector<int> competitors(N);
    for (int i = 0; i < N; i++) {
        cin >> competitors[i];
    }
    
    sort(competitors.begin(), competitors.end());
    vector<pair<int, int>> results;
    cin >> P;
    for (int i = 0; i < P; i++) {
        int markPower;
        cin >> markPower;
        int winCount = binary_search(competitors, markPower);
        int powerSum = 0;
        for (int j = 0; j < winCount; j++) {
            powerSum += competitors[j];
        }
        results.emplace_back(winCount, powerSum);
    }
    
    for (const auto& result : results) {
        cout << result.first << " " << result.second << endl;
    }

    return 0;
}
