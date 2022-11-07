// ***Piece of Cake! Solution***
// Difficulty: 1.5
// Time Limit: 1 second, Memory Limit: 1024 MB
// Acceptance: 63%
// CPU Time: 0.00 s
// Author: Zachary Friggstad
// Source: Rocky Mountain Regional Programming Contest 2019
// Link: https://open.kattis.com/problems/pieceofcake2


#include <bits/stdc++.h>
using namespace std;
 
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
 
#define pb push_back
#define mp make_pair


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, h, v; cin >> n >> h >> v;
    int ans = 0;
    ans = max(ans, h * v);
    ans = max(ans, (n - h) * v);
    ans = max(ans, h * (n - v));
    ans = max(ans, (n - h) * (n - v));
    cout << ans * 4 << endl;

    return 0;
}
