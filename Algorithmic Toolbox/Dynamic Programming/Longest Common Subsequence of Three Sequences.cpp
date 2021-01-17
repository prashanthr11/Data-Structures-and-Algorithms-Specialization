#include <bits/stdc++.h>


using namespace std;


int LCS(vector<int> s1, vector<int> s2, vector<int> s3){
    int m = s1.size();
    int n = s2.size();
    int o = s3.size();
    int dp[m + 1][n + 1][o + 1];
    memset(dp, 0, sizeof(dp));
    
    if(m == 0 || n == 0 || o == 0)
    return 0;




    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= o; k++) {
            if (s1[i - 1] == s2[j - 1] and s2[j - 1] == s3[k - 1])   // Found Match
                dp[i][j][k] = 1 + dp[i - 1][j - 1][k - 1];
            
            else 
                dp[i][j][k] = max(dp[i][j][k - 1], max(dp[i][j - 1][k], dp[i - 1][j][k]));
            }
        }
    }
    
    return dp[m][n][o];
}




int main()
{
    int n, m, o;
    cin >> n;
    vector<int> a(n);
    
    for(auto i = 0; i < n; ++i)
    cin >> a[i];
    
    cin >> m;
    vector<int> b(m);
    
    for(auto i = 0; i < m; ++i)
    cin >> b[i];
    
    cin >> o;
    vector<int> c(o);
    
    for(auto i = 0; i < o; ++i)
    cin >> c[i];
    
    cout << LCS(a, b, c) << endl;
}