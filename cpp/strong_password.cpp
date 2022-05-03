#include "bits/stdc++.h"
using namespace std;

const int N = 200005;

int get(char c) {
   if(c >= '0' && c <= '9') return 0;
   if(c >= 'a' && c <= 'z') return 1;
   if(c >= 'A' && c <= 'Z') return 2;
   return 3;
}

int minimumNumber(int n, string password) {
    // Return the minimum number of characters to make the password strong
    int num = 1, spec = 1, low=1, cap=1, rest = 2;
    string special_characters = "!@#$%^&*()-+";
    for(int i =0; i < password.size() ; i++) {
        if(num!=0 && password[i] >='0' && password[i]<='9')
            num--;
        else if(low!=0 && password[i]>='a' && password[i]<='z') 
            low--;
        
        else if(cap!= 0 && password[i]>='A' && password[i]<='Z')
            cap--;       
        
        else if(spec!=0 && special_characters.find(password[i]) != special_characters.npos) 
            spec--;
        
        else if(rest !=0) 
            rest--;
        
        else if(num==cap==spec==rest==0)    
            break;
    }
    return num+spec+low+cap+rest;
}

int main() {
   int n;
   string s;

   cin >> n;
   cin >> s;

   int ans = 0;

   for(int i = 0; i < n; i++) {
      ans |= (1 << get(s[i]));
   }

   cout << max(6 - n, 4 - __builtin_popcount(ans));
   return 0;
}
