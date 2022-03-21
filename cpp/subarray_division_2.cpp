/*
We're going to solve this problem using a brute force approach by looping through the squares in the chocolate bar at each possible interval of squares that can form a piece of length  and summing the values of the squares within that interval. If that sum is equal to , we increment the integer that stores the number of ways the chocolate can be shared with Ron. Once we finish traversing through all possible intervals, we print the number of ways we can satisfy the constraints as output.

Tip: Be sure to set up your loop to prevent 'array index out of bounds' errors!
*/

#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> c(n);
    for(int i = 0; i < n; i++){
       cin >> c[i];
    }
    int d;
    int m;
    cin >> d >> m;

    int ans = 0;
    for(int i = 0; i < n; i++){
        if (i + m - 1 < n){
            int sum = 0;
            for (int j = i; j <= i + m - 1; j++){
                sum = sum + c[j];
            }
            if (sum==d) {
                ans++;
            }
        }
    }
    cout << ans << endl;
    return 0;
}

// We can also solve this challenge in  time (see Tester solution below). Java


