#include <iostream>
#include <cstring>
using namespace std;

string s;
int dp[2501];
int check[2501][2501];


int isPal(int start,int end){
    if(start >= end){
        return 1;
    } else if (check[start][end] != -1){
        return check[start][end];
    } else if (s[start-1] != s[end-1]){
        check[start][end] = 0;
    } else {
        check[start][end] = isPal(start+1,end-1);
    }
    return check[start][end];
}

int main(){
    cin>>s;

    for(int i=1; i<=s.size();i++){
        for(int j=1; j<=s.size();j++){
            check[i][j] = -1;
        }
    }

    for(int end=1; end<=s.size(); end++){
        dp[end] = s.size();
        for(int start=1; start<=end; start++){
            if(isPal(start,end)){
                dp[end] = min(dp[end], dp[start-1]+1);
            }
        }
    }
    cout<<dp[s.size()];
}