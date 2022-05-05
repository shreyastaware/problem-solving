#include <bits/stdc++.h>
#include <assert.h>
using namespace std;

int A[10004];
int B[10004];

int main() {
  int n, m, x;

  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> x;
    A[x]++;
  }

  cin >> m;
  for (int i = 0; i < m; i++) {
    cin >> x;
    B[x]++;
  }

  assert(m >= n);

  for (int i = 1; i <= 10000; i++) {
    if (B[i] > A[i])
      cout << i << " ";
  }
  cout << "\n";
}
