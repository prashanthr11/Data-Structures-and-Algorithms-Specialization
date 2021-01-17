#include <bits/stdc++.h>

using namespace std;

int LCS(vector<int> s1, vector<int> s2){
    int m = s1.size();
    int n = s2.size();
    
    int dp[m + 1][n + 1];
    memset(dp, 0, sizeof(dp));
    
    if(m == 0 || n == 0)
    return 0;

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
        if (s1[i - 1] == s2[j - 1])   // Found Match
            dp[i][j] = 1 + dp[i - 1][j - 1];
        
        else 
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j]);
        }
    }
    
    return dp[m][n];
}


int main()
{
    int n, m;
    cin >> n;
    vector<int> a(n);
    
    for(auto i = 0; i < n; ++i)
    cin >> a[i];
    
    cin >> m;
    vector<int> b(m);
    
    for(auto i = 0; i < m; ++i)
    cin >> b[i];
    
    cout << LCS(a, b) << endl;
}
