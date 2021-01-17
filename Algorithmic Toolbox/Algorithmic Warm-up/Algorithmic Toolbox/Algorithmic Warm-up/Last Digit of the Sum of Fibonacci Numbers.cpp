#include <bits/stdc++.h>

#define int long long

using namespace std;

class xyz {
  public:
    int pre[60], arr[60];
    xyz() {
        memset(arr, 0, sizeof(arr));
        memset(pre, 0, sizeof(pre));
        
        arr[0] = 0;
        arr[1] = 1;
        for(int i = 2; i < 60; ++i)
            arr[i] = (arr[i - 1] % 10 + arr[i - 2] % 10) % 10;
        
        pre[0] = 0;
        pre[1] = 1;
        
        for(int i = 2; i < 60; ++i) 
            pre[i] = pre[i - 1] + (arr[i - 1] % 10 + arr[i - 2] % 10) % 10;
            
    }
    
    int ans(int n) {
        return (pre[n % 60] + 10) % 10;
    }
};


signed main()
{
    int n;
    cin >> n;
    xyz obj;
    cout << obj.ans(n) << endl;
    
    return 0;
}

