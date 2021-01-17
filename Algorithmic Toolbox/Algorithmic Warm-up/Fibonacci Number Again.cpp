#include <bits/stdc++.h>

#define int long long

using namespace std;

int a = 0, b = 1, c = 0;

int pisano(int x) {
    for(int i = 0; i < x * x; ++i) {
        c = (a + b) % x;
        a = b;
        b = c;
        
        if(a == 0 && b == 1)
            return i + 1;
    }
}


int get_fib(int x, int y) {
    int arr[x + 2];
    arr[0] = 0;
    arr[1] = 1;
    for(int i = 2; i <= x; ++i)
        arr[i] = arr[i - 1] % y + arr[i - 2] % y;
    
    return (arr[x] + y) % y;
}

int fib(int n, int m) {
    int z =  n % pisano(m);
    return get_fib(z, m);
}

signed main()
{
    int n, m;
    cin >> n >> m;
    cout << fib(n, m) << endl;
    return 0;
}
