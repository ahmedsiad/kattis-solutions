// ***The Grand Adventure Solution***
// Difficulty: 2.0
// Time Limit: 1 second, Memory Limit: 1024 MB
// Acceptance: 43%
// CPU Time: 0.00 s
// Author: Dillon Cutaiar
// Source: 2018 Virginia Tech High School Programming Contest
// Link: https://open.kattis.com/problems/thegrandadventure


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

    int t; cin >> t;
    map<char, char> mp = {{'b', '$'}, {'j', '*'}, {'t', '|'}};

    while (t--) {
        string line; cin >> line;
        stack<char> stack;
        bool flag = true;
        rep(i, 0, line.length()) {
            if (line[i] == '.') continue;
            if (mp.find(line[i]) == mp.end()) {
                stack.push(line[i]);
            }
            else {
                //cout << stack.top() << " " << line[i] << endl;
                if (stack.empty() || mp[line[i]] != stack.top()) {
                    flag = false; break;
                }
                stack.pop();
            }
        }

        if (!stack.empty()) flag = false;
        cout << (flag ? "YES" : "NO") << endl;
    }
    return 0;
}
