// ***Delimiter Soup Solution***
// Difficulty: 2.2
// Time Limit: 1 second, Memory Limit: 1024 MB
// Acceptance: 53%
// CPU Time: 0.00 s
// Author: Jean Niklas L'orange
// Source: IDI Open 2019
// Link: https://open.kattis.com/problems/delimitersoup


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

    int l; cin >> l;
    int i = 0;
    stack<char> stck;

    bool flag = true;
    string s;
    getline(cin, s);
    getline(cin, s);
    map<char, char> expected;
    expected['['] = ']'; expected['('] = ')'; expected['{'] = '}';
    rep(i, 0, l) {
        if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
            stck.push(s[i]);
        }
        else if (s[i] != ' ') {
            if (stck.empty()) {
                flag = false;
                cout << s[i] << " " << i << endl; break;
            }
            char top; top = stck.top();
            stck.pop();
            if (expected[top] != s[i]) {
                flag = false;
                cout << s[i] << " " << i << endl;
                break;
            }
        }
    }
    if (flag) cout << "ok so far" << endl;
    return 0;
}
