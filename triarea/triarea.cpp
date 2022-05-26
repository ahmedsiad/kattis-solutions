// ***Triangle Area Solution***
// Difficulty: 1.3
// Time Limit: 1 second, Memory Limit: 1024 MB
// CPU Time: 0.00 s
// Author: Johan Sannemo
// Source: Principles of Algorithmic Problem Solving
// Link: https://open.kattis.com/problems/triarea


#include <iostream>

using namespace std;

int main()
{
    float a, b;
    while (cin >> a >> b) {
        cout << (a * b)/2 << endl;
    }
    return 0;
}
