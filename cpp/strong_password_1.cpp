#include "bits/stdc++.h"
using namespace std;

const int N = 200005;

const string numbers = "0123456789";
const string lower_case = "abcdefghijklmnopqrstuvwxyz";
const string upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const string special = "!@#$%^&*()-+";

int main() {

   map <char, int> m;

   for(auto c: numbers)
      m[c] = 0;
   for(auto c: lower_case)
      m[c] = 1;
   for(auto c: upper_case)
      m[c] = 2;
   for(auto c: special)
      m[c] = 3;
   
   set <int> types;

   int n; string s;

   cin >> n;
   cin >> s;

   for(auto c: s) {
      types.insert(m[c]);
   }

   cout << max(6 - n, 4 - (int)types.size());
   return 0;
}