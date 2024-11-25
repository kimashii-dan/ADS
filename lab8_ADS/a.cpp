#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>

using namespace std;

int main() {
    while (true) {
        int N;
        cin >> N;
        if (N == 0) break;  // End of input

        vector<string> patterns(N);
        for (int i = 0; i < N; i++) {
            cin >> patterns[i];
        }
        
        string text;
        cin >> text;

        unordered_map<string, int> frequency_map;

        // Count occurrences of each pattern in the text
        for (const string& pattern : patterns) {
            int count = 0;
            size_t pos = text.find(pattern, 0);
            while (pos != string::npos) {
                count++;
                pos = text.find(pattern, pos + 1);
            }
            frequency_map[pattern] = count;
        }

        // Find the maximum frequency
        int max_frequency = 0;
        for (const auto& entry : frequency_map) {
            if (entry.second > max_frequency) {
                max_frequency = entry.second;
            }
        }

        // Output dominating patterns in order of input
        for (const string& pattern : patterns) {
            if (frequency_map[pattern] == max_frequency) {
                cout << pattern << endl;
            }
        }
    }
    return 0;
}
