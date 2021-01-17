#include <bits/stdc++.h>

#define int long long

using namespace std;

class xyz {
  public:
    int arr[60], pre[60], ans[60];
    xyz() {
        memset(arr, 0, sizeof(arr));
        memset(pre, 0, sizeof(pre));
        memset(ans, 0, sizeof(ans));

        arr[0] = 0;
        arr[1] = 1;

        ans[0] = 0;
        ans[1] = 1;

        for(int i = 2; i < 60; ++i) {
            arr[i] = arr[i - 1] + arr[i - 2];
            ans[i] = pow((arr[i - 1] % 10 + arr[i - 2] % 10) % 10, 2);
        }


        for(auto i = 0; i < 60; ++i)
            ans[i] = ans[i] % 10;


        pre[0] = 0;

        for(auto i = 1;i < 60; ++i)
            pre[i] = (pre[i - 1] + ans[i]) % 10;

    }

    int op(int n) {
        return pre[n] % 10;
    }
};


signed main()
{
    int n;
    cin >> n;
    xyz obj;
    cout << obj.op(n % 60) << endl;

    return 0;
}


