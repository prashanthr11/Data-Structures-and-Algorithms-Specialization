#include <bits/stdc++.h>

#define int long long

using namespace std;

int lcm_naive(int a, int b, int c) {
   return (a / c) * b;
    
}

int gcd_fast(int a, int b) {
   
    if(b == 0)
        return a;
    else
        gcd_fast(b, a % b);
}

signed main() {
  int a, b;
  std::cin >> a >> b;
  std::cout << lcm_naive(a, b, gcd_fast(a,b)) << std::endl;
  return 0;
}

