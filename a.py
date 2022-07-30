N = int(input())
S = list(input())

if S[0] == S[N-1]:
    pass
else:
    if S[0] == 'B':
        S[0] = 'A'
        S[1] = 'B'
    else:
        pass

for i in range(1, int(N/2)):
    if S[i] == S[N-i-1]:
        continue
    else:
        if S[i] == 'B':
            S[i] = 'A'
            S[i+1] = 'B'
        else:
            if S[N-i] == 'B':
                S[N-i-1] = 'A'
            elif S[i-1] == 'A':
                S[i] = 'B'

check = True
for i in range(int(N/2)):
    if S[i] == S[N-i-1]:
        pass
    else:
        check = False

print('Yes' if check else 'No')
