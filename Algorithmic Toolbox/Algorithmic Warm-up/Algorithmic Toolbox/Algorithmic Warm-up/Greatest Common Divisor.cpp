#include <bits/stdc++.h>

#define int long long

using namespace std;

int gcd_fast(int a, int b) {
    
    if(b == 0)
        return a;
    else
        gcd_fast(b, a % b);
}



signed main() {
    int n, m;
    cin >> n >> m;

    cout << gcd_fast(n, m) << ' ';
    return 0;
}

 
    
