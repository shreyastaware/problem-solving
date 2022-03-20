t = input()
    
for i in range(t):
    n,k = map(int, input().strip().split())
    
    A = map(int, input().strip().split())
    A.sort()
    
    B = map(int, input().strip().split())
    B.sort(reverse=True)
    
    answer = True
    for a,b in zip(A,B):
        if a+b < k:
            answer = False
    if answer:
        print("YES")
    else:
        print("NO")