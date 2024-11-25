// #include <iostream>
// #include <cmath>
// using namespace std;
// int main() {
//     int n;
//     cin >> n;
//     for (int i = 2; i <= sqrt(n); i++) {
//         int count = 0;
//         while (n % i == 0) {
//             count++;
//             n /= i;
//         }
//         if (count > 0) {
//             cout << i << "^" << count;
//             if (n > 1) cout << " * ";
//         }
//     }
//     if (n > 1) {
//         cout << n << "^1";
//     }
//     cout << endl;
//     return 0;
// }



// #include <iostream>
// #include <stack>
// #include <vector>

// using namespace std;

// int main() {
//     int n;
//     cin >> n;
//     vector<int> a(n), result(n, -1);
//     stack<int> st;

//     for (int i = 0; i < n; ++i) {
//         cin >> a[i];
//         while (!st.empty() && a[st.top()] > a[i]) {
//             st.pop();
//         }
//         if (!st.empty()) {
//             result[i] = a[st.top()];
//         }
//         st.push(i);
//     }

//     for (int i = 0; i < n; ++i) {
//         cout << result[i] << " ";
//     }
//     return 0;
// }



#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin >> n;
    
    vector<int> meow(n);
    for (int i = 0; i < n; ++i) {
        cin >> meow[i];
    }
    
    int k;
    cin >> k;
    
    int min_diff = abs(k - meow[0]);
    int pos = 0;
    
    for (int i = 1; i < n; ++i) { // Start from 1 since we've already considered index 0
        int diff = abs(k - meow[i]);
        if (diff < min_diff) {
            min_diff = diff;
            pos = i;
        }
    }
    
    cout << pos << endl;
    return 0;
}
