// ***Union-Find Solution***
// Difficulty: 4.7
// Time Limit: 1 second, Memory Limit: 1024 MB
// Acceptance: 31%
// CPU Time: 0.22 s
// Author: Per Austrin
// Source: KTH CSC Popup spring 2013
// Link: https://open.kattis.com/problems/unionfind


#include <bits/stdc++.h>
using namespace std;
 
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
 
#define pb push_back
#define mp make_pair

int dsu[10000001];
int find(int a) {
    if (dsu[a] == a) return a;
    return dsu[a] = find(dsu[a]);
}
void join(int a, int b) {
    dsu[find(a)] = find(b);
}
bool same(int a, int b) {
    return find(a) == find(b);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, q;
    cin >> n >> q;

    rep(i, 0, n) {
        dsu[i] = i;
    }

    while (q--) {
        char op;
        int a; int b;
        cin >> op >> a >> b;
        if (op == '?') {
            if (same(a, b)) cout << "yes" << "\n";
            else cout << "no" << "\n";
        }
        else {
            join(a, b);
        }
    }

    return 0;
}
