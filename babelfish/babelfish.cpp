// ***Babelfish Solution***
// Difficulty: 2.5
// Time Limit: 3 seconds, Memory Limit: 1024 MB
// Acceptance: 43%
// CPU Time: 0.22 s
// Author: No author
// Source: Waterloo Programming Contest 2001-09-22
// Link: https://open.kattis.com/problems/babelfish


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

    map<string, string> dict;
    string line;
    while (getline(cin, line)) {
        if (line == "") break;
        int idx = line.find(' ');
        dict[line.substr(idx + 1)] = line.substr(0, idx);
    }

    string s3;
    while (cin >> s3) {
        if (dict.find(s3) != dict.end()) {
            cout << dict[s3] << endl;
        } else cout << "eh" << endl;
    }

    return 0;
}
