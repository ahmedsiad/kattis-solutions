// ***Chess Tournament Solution***
// Difficulty: 6.1
// Time Limit: 4 seconds, Memory Limit: 1024 MB
// Acceptance: 32%
// CPU Time: 0.06 s
// Author: Mees de Vries
// Source: Benelux Algorithm Programming Contest (BAPC) preliminaries 2016
// Link: https://open.kattis.com/problems/chesstournament


#include <bits/stdc++.h>
using namespace std;
 
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
 
#define pb push_back
#define mp make_pair

int MAXN = 100000;
vector<int> visited(MAXN, 0);


vector<int> par(MAXN, 0);

int getPar(int x) {
  if (par[x] == x) return x;
  return par[x] = getPar(par[x]);
}
bool same(int x, int y) {
    return getPar(x) == getPar(y);
}
void Union(int x, int y) {
  par[getPar(x)] = getPar(y);
}


bool dfs(int node, int parent, vector<vector<int>> &g) {
    visited[node] = 1;

    for (auto nb : g[node]) {
        //cout << node << " " << nb << " " << visited[nb] << " " << parent << endl;
        if (visited[nb] == 1 && nb != parent) return false;
        if (visited[nb] == 0) {
            bool ans = dfs(nb, node, g);
            if (!ans) return false;
        }
    }
    visited[node] = 2;
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;
    
    rep(i, 0, MAXN) par[i] = i;

    vector<vector<int>> graph(n, vector<int>());
    rep(i, 0, m) {
        int u, v;
        string op;
        cin >> u >> op >> v;
        if (op == ">") {
            graph[u].pb(v);
        }
        else if (op == "<") {
            graph[v].pb(u);
        }
        else {
            if (!same(u, v)) {
                Union(u, v);
            }
        }
    }

    rep(i, 0, n) {
        if (par[i] != i) {
            graph[i].pb(par[i]);
            graph[par[i]].pb(i);
        }
    }

    bool ans = true;
    rep(i, 0, n) {
        if (visited[i] == 0) {
            bool visit = dfs(i, -1, graph);
            ans = ans & visit;
        }
    }

    if (ans) cout << "consistent" << endl;
    else cout << "inconsistent" << endl;
    return 0;
}
