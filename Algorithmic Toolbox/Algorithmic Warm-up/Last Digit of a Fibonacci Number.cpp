#include <bits/stdc++.h>

#define int long long

using namespace std;

int get_fibonacci_last_digit_fast(int n) {
    int a[n];
    a[0] = 0;
    a[1] = 1;

    for(int i = 2; i <= n; i++)
        a[i] = (a[i - 1] + a[i - 2]) % 10;

    return a[n];
}



signed main() {
    int n = 0;
    cin >> n;

    cout << get_fibonacci_last_digit_fast(n) << ' ';
    return 0;
}
