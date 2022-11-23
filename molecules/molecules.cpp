// ***Molecules Solution***
// Difficulty: 3.7
// Time Limit: 2 seconds, Memory Limit: 1024 MB
// Acceptance: 33%
// CPU Time: 0.00 s
// Author: No author
// Source: Rocky Mountain Regional Programming Contest 2019
// Link: https://open.kattis.com/problems/molecules


#include <bits/stdc++.h>
using namespace std;
 
#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
 
#define pb push_back
#define mp make_pair

typedef vector<double> vd;
const double eps = 1e-12;

int solveLinear(vector<vd>& A, vd& b, vd& x) {
    int n = sz(A), m = sz(x), rank = 0, br, bc;
    if (n) assert(sz(A[0]) == m);
    vi col(m); iota(all(col), 0);

    rep(i,0,n) {
        double v, bv = 0;
        rep(r,i,n) rep(c,i,m)
            if ((v = fabs(A[r][c])) > bv)
                br = r, bc = c, bv = v;
        if (bv <= eps) {
            rep(j,i,n) if (fabs(b[j]) > eps) return -1;
            break;
        }
        swap(A[i], A[br]);
        swap(b[i], b[br]);
        swap(col[i], col[bc]);
        rep(j,0,n) swap(A[j][i], A[j][bc]);
        bv = 1/A[i][i];
        rep(j,i+1,n) {
            double fac = A[j][i] * bv;
            b[j] -= fac * b[i];
            rep(k,i+1,m) A[j][k] -= fac*A[i][k];
        }
        rank++;
    }

    x.assign(m, 0);
    for (int i = rank; i--;) {
        b[i] /= A[i][i];
        x[col[i]] = b[i];
        rep(j,0,i) b[j] -= A[j][i] * b[i];
    }
    return rank; // (multiple solutions if rank < m)
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n; int m; cin >> n >> m;
    map<int, pii> fixed;
    vector<vector<int>> graph(n, vector<int>());
    rep(i, 0, n) {
        int x, y; cin >> x >> y;
        if (x != -1 || y != -1) {
            fixed[i] = mp(x, y);
        }
    }
    rep(i, 0, m) {
        int a, b; cin >> a >> b;
        a--; b--;
        graph[a].pb(b);
        graph[b].pb(a);
    }
    vector<vd> matx(n, vd(n, 0));
    vector<vd> maty(n, vd(n, 0));
    vd bx(n, 0);
    vd by(n, 0);

    rep(i, 0, n) {
        if (fixed.find(i) == fixed.end()) {
            int length = graph[i].size();
            matx[i][i] = -length;
            maty[i][i] = -length;

            for (auto j : graph[i]) {
                matx[i][j] = 1;
                maty[i][j] = 1;
            }
        }
        else {
            matx[i][i] = 1;
            maty[i][i] = 1;
            bx[i] = fixed[i].first;
            by[i] = fixed[i].second;
        }
    }

    vd xs(n, 0);
    vd ys(n, 0);
    int r1 = solveLinear(matx, bx, xs);
    int r2 = solveLinear(maty, by, ys);

    rep(i, 0, n) {
        if (fixed.find(i) != fixed.end()) {
            cout << fixed[i].first << " " << fixed[i].second << endl;
        }
        else {
            cout << xs[i] << " " << ys[i] << endl;
        }
    }
    return 0;
}
