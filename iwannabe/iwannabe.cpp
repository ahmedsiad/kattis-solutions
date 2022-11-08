// ***I Wanna Be The Very Best Solution***
// Difficulty: 2.6
// Time Limit: 1 second, Memory Limit: 1024 MB
// Acceptance: 37%
// CPU Time: 0.00 s
// Author: No author
// Source: The 2018 ICPC Vietnam National Programming Contest
// Link: https://open.kattis.com/problems/iwannabe


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

    ll n, k; cin >> n >> k;
    vector<pair<ll, ll>> atk, def, hp;
    rep(i, 0, n) {
        ll a, d, h; cin >> a >> d >> h;
        atk.pb(make_pair(a, i));
        def.pb(make_pair(d, i));
        hp.pb(make_pair(h, i));
    }

    sort(atk.begin(), atk.end(), [](auto a, auto b) { return a.first > b.first;});
    sort(def.begin(), def.end(), [](auto a, auto b) { return a.first > b.first;});
    sort(hp.begin(), hp.end(), [](auto a, auto b) { return a.first > b.first;});

    set<ll> ans;
    rep(i, 0, k) {
        ans.insert(atk[i].second);
        ans.insert(def[i].second);
        ans.insert(hp[i].second);
    }
    cout << ans.size() << endl;
    return 0;
}
