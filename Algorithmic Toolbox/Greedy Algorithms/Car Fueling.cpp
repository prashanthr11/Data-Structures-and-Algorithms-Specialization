#include <bits/stdc++.h>

using namespace std;

int check(int dist,int mil,int n,int *a){
    int cnt = 0, temp = mil;
    if(dist < mil)
        return 0;

    for(int i = 0; i <= n; i++) {
        if(abs(a[i + 1] - a[i]) > mil) {
            return -1;
        }
    }
    
    for(int i = 0; i <= n + 1; i++) {
        if(a[i] > mil) {
            mil = a[i - 1] + temp;
            cnt++;
            i--;
        }
        else if(a[i] == mil) {
            if (a[i] == dist)
                return cnt;
            mil = a[i] + temp;
            cnt++;
            i--;
        }
    }
    
    return cnt;
}

int main() {
    int m, n, d;
    cin >> d >> m >> n;
    int a[n + 1];
    a[0] = 0;
    for(int i = 1;i <= n + 1; i++)
        cin >> a[i];

    a[n + 1]=d;
    cout << check(d, m, n, a);
    return 0;
}
