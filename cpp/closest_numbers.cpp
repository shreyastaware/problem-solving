#include <bits/stdc++.h>

using namespace std;

vector <int> ans;
int arr [200000 + 10];

int main()
{
    int n;
    
    cin >> n;
    
    for(int i = 0; i < n; i++)
        cin >> arr[i];
    
    sort(arr, arr + n);
    
    int mini = INT_MAX;
    
    for(int i = 1; i < n; i++){
        
        if(arr[i] - arr[i - 1] <= mini){
            if(arr[i] - arr[i - 1] < mini) 
                ans.clear();
            
            mini = arr[i] - arr[i - 1];
            ans.push_back(arr[i - 1]);
            ans.push_back(arr[i]);
        }
    }
    
    for(int i = 0; i < ans.size(); i++){
        cout << ans[i] << " ";
    }
    
    return 0;
}

