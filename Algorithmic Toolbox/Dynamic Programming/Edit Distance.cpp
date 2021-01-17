#include <bits/stdc++.h>

using namespace std;

int editDistance(string s1, string s2){
    int m = s1.size();
    int n = s2.size();
    int dp[m + 1][n + 1];
    memset(dp, 0, sizeof(dp));

    for (int i = 0; i <= m; i++) 
        dp[i][0] = i;
    
    for (int j = 0; j <= n; j++) 
        dp[0][j] = j;
    

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
        if (s1[i - 1] == s2[j - 1]) dp[i][j] = dp[i - 1][j - 1];
            else dp[i][ j] = 1 + min(min(dp[i][j - 1], dp[i - 1][j]), dp[i - 1][j - 1]);
        }
    }
    
    
    return dp[m][n];
}


int main()
{
    string s1, s2;
    getline(cin, s1);
    getline(cin, s2);
    cout << editDistance(s1, s2) << endl;
}
