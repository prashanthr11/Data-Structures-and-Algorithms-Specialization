#include <bits/stdc++.h>
#include <iostream>
#define int long long
using namespace std;


vector<int> optimal_summands(int n) {
  vector<int> summands;
  if (n == 1) {
      summands.push_back(1);
      return summands;
  }
  if (n == 2) {
      summands.push_back(2);
      return summands;
  }
  int cnt = 0, sumi = 1;
  
  for(auto i = 1; i < 2; i++) {
    summands.push_back(i);
      for(auto j = i + 1; j < n; ++j) {
          if(abs(n - j) > sumi) {
              summands.push_back(j);
              sumi += j;
            ++cnt;
          }
          else
          break;
      }
  }
  
  
  if(n - sumi <= summands[cnt]) {
      summands[cnt] += n - sumi;
  }
  else {
      summands.push_back(n - sumi);
  }
  
  return summands;
}


signed main() {
ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
  int n;
  cin >> n;
  vector<int> summands = optimal_summands(n);
  std::cout << summands.size() << '\n';
  for (size_t i = 0; i < summands.size(); ++i) 
    std::cout << summands[i] << ' ';

}
