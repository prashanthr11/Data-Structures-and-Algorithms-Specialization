#include <bits/stdc++.h>

using namespace std;

unordered_map<char, int> mp;
unordered_map<int, char> mp2;
static int cnt = 0;

struct Trie {
    struct Trie *root[4] = {0};
    int count = 0;
};


void add(struct Trie *head, string s) {
    auto tmp = head;
    
    for(auto i:s) {
        if (tmp -> root[mp[i]])
            tmp = tmp -> root[mp[i]];
        else {
            cnt++;
            auto temp = new struct Trie;
            tmp -> root[mp[i]] = temp;
            temp -> count = cnt;
            tmp = temp;
        }
    }
    tmp = head;
}


void print(struct Trie* head) {
    for(auto i = 0; i < 4; ++i) {
        if(head -> root[i]) {
            cout << head -> count << "->"  << head -> root[i] -> count << ":" << mp2[i] << '\n';
            print(head -> root[i]);
        }
    }
}

int main()
{
    auto head = new struct Trie();
    
    int n;
    cin >> n;
    
    auto ct = 0;
    
    string s2 = "ACGT";
    
    for(auto i:s2) {
        mp2[ct] = i;
        mp[i] = ct;
        ct++;
    }
        
    for(auto i = 0; i < n; ++i) {
        string s;
        cin >> s;
        add(head, s);
    }
    
    print(head);
    
    return 0;
}
