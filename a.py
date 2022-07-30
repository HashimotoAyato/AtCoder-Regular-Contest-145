N = int(input())
S = list(input())

if S[0] == S[-1]:
    check = True
else:
    if S[0] == 'B':
        S[-1] = 'B'
        S[-2] = 'A'
        check = True
    else:
        check = False

for i in range(1, int(N/2)):
    if S[i] == S[N-i-1]:
        


for i in range(int(N/2)):
    if S[i] == S[N-i-1]:
        pass
    else:
        check = False

print('Yes' if check else 'No')
