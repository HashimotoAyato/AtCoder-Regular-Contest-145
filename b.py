N, A, B = map(int, input().split())

if A <= B:
    if A-1 <= N:
        print(N-A+1)
    else:
        print(0)

else:
    if A-1 <= N:
        ans = 0
        ans += int(((N-A+1) - ((N-A+1)%A)) / A) * B
        if (N-A+1)%A <= B:
            ans += (N-A+1)%A
        else:
            ans += B
    else:
        ans = 0
    print(ans)
