#include <iostream>
#include <vector>
#include <queue>
using namespace std;

const int MAXN = 1000;
vector<int> tree[MAXN];
int levels[MAXN];

void bfs(int root) {
    queue<pair<int, int>> q;
    q.push({root, 1});
    
    while (!q.empty()) {
        int node = q.front().first;
        int level = q.front().second;
        q.pop();
        
        levels[level]++;
        

        for (int child : tree[node]) {
            q.push({child, level + 1});
        }
    }
}

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n - 1; i++) {
        int x, y, z;
        cin >> x >> y >> z;
        tree[x].push_back(y);
    }


    bfs(1);


    int max_width = 0;
    for (int i = 1; i <= n; i++) {
        if (levels[i] > max_width) {
            max_width = levels[i];
        }
    }

    cout << max_width << endl;

    return 0;
}
