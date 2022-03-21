#include <bits/stdc++.h>
using namespace std;
#define sz(x) ((int) (x).size())
#define forn(i,n) for (int i = 0; i < int(n); ++i)
typedef long long ll;
typedef long long i64;
typedef long double ld;
const int inf = int(1e9) + int(1e5);
const ll infl = ll(2e18) + ll(1e10);

const int maxn = 100100;

int n;
int a[maxn];

int main() {
    #ifdef LOCAL
    assert(freopen("test.in", "r", stdin));
    #endif
    cin >> n;
    forn (i, n)
        cin >> a[i];
    sort(a, a + n);
    reverse(a, a + n);
    forn (i, n - 2) {
        if (a[i + 2] + a[i + 1] <= a[i])
            continue;
        cout << a[i + 2] << ' ' << a[i + 1] << ' ' << a[i] << '\n';
        return 0;
    }
    cout << -1 << '\n';
}