#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, d;
    if (!(cin >> n >> m >> d)) return 0;
    vector<string> g(n);
    for (int i = 0; i < n; ++i) cin >> g[i];

    const int INF = 1e9;
    vector<vector<int>> dist(n, vector<int>(m, INF));

    // init
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
            if (g[i][j] == 'x' || g[i][j] == 'X') dist[i][j] = 0;

    // forward pass
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (i) dist[i][j] = min(dist[i][j], dist[i-1][j] + 1);
            if (j) dist[i][j] = min(dist[i][j], dist[i][j-1] + 1);
        }
    }
    // backward pass
    for (int i = n-1; i >= 0; --i) {
        for (int j = m-1; j >= 0; --j) {
            if (i+1 < n) dist[i][j] = min(dist[i][j], dist[i+1][j] + 1);
            if (j+1 < m) dist[i][j] = min(dist[i][j], dist[i][j+1] + 1);
        }
    }

    // maximal square on safe cells
    int ans = 0;
    vector<int> prev(m+1, 0), cur(m+1, 0);
    for (int i = 1; i <= n; ++i) {
        fill(cur.begin(), cur.end(), 0);
        for (int j = 1; j <= m; ++j) {
            if (dist[i-1][j-1] >= d) {
                cur[j] = 1 + min({cur[j-1], prev[j], prev[j-1]});
                ans = max(ans, cur[j]);
            }
        }
        swap(prev, cur);
    }

    cout << ans << "\n";
    return 0;
}
