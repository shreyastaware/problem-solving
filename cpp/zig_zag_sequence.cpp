#include <bits/stdc++.h>
using namespace std;

int N; int A[10005];

void findZigZagSequence(){ 
    
    sort(A + 1, A + N + 1); 
    int mid = (N + 1)/2; 
    swap(A[mid], A[N]);

    int st = mid + 1;
    int ed = N - 1;
    while(st <= ed)
    {
        swap(A[st], A[ed]);
        st++;
        ed--;
    }
}

set Set;

int main() { 
    #ifdef forthright48 freopen ( "input00.txt", "r", stdin ); 
    freopen ( "output00.txt", "w", stdout ); 
    #endif // forthright48

    int test_cases;
    cin >> test_cases;
    assert(test_cases>=1 && test_cases<=20);
    for(int cs = 1; cs <= test_cases; cs++){
        cin >> N;
        Set.clear();
        assert(N>=1 && N<=10000);
        for(int i = 1; i <= N; i++){
            cin >> A[i];
            Set.insert(A[i]);
            assert(A[i]>=1 && A[i]<=1000000000);
        }
        int Sz = Set.size();
        assert(N == Sz);
        findZigZagSequence();
        for(int i = 1; i <= N; i++){
            if(i > 1) printf(" ");
            printf("%d", A[i]);
        }
        printf("\n");
    }
}
