#include <bits/stdc++.h>

using namespace std;

int fibonacci_fast(int n) {
    int a[n];
    a[0] = 0;
    a[1] = 1;

    for(int i = 2; i <= n; i++)
        a[i] = a[i - 1] + a[i - 2];

    return a[n];
}



int main() {
    int n = 0;
    cin >> n;

    cout << fibonacci_fast(n) << ' ';
    return 0;
}

