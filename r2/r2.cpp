// ***R2 Solution***
// Difficulty: 1.3
// Time Limit: 1 second, Memory Limit: 1024 MB
// CPU Time: 0.00 s
// Author: No author
// Source: Croatian Open Competition in Informatics 2006/2007, contest #2
// Link: https://open.kattis.com/problems/r2


#include <iostream>

using namespace std;

int main()
{
    long long a,b;
    while (cin >> a >> b)
    {
        cout << (b - a) + b << endl;
    }
    return 0;
}
