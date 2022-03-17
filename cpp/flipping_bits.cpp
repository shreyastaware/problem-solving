// Nothing special is required to solve this problem. You have only to properly use the '~' bitwise NOT operator. Special care should be taken in languages with no unsigned integers to avoid overflows.

#include <cstdio>
using namespace std;

int main() {
    register int N;
    unsigned int x;
    for (scanf("%d", &N); N; --N) {
        scanf("%u", &x);
        printf("%u\n", ~x);
    }
    return 0;
}
