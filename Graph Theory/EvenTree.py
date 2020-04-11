#include <bits/stdc++.h>
using namespace std;

struct node{ int parent, children = 0; };

int main(){
    int n, o, p, result = 0;
    cin >> n >> o;
    vector<node> tree(n+1);
    while(cin >> o >> p){
        tree[o].parent = p;
        tree[p].children++; 
    }  
    for(int i = n; i > 1; i--)
        if(tree[i].children % 2){
            tree[tree[i].parent].children--;
            result++;    
        }   
    cout << result;
    return 0;
}
