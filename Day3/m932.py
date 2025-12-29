move_r=[-1, 0, 1, 1, 0, -1]
move_c=[1, 1, 0, -1, -1, 0]

m, n, k=map(int, input().split())
strings=[]
for i in range(m):
    s=input()
    strings.append(list(s))
    for j in range(m-i-1):
        strings[i].insert(0, " ")
    for k in range(i):
        strings[i].append(" ")
for r in strings:
    print(*r)
move=list(map(int, input().split()))
cur_r, cur_c=m-1, 0
letters=""
for mv in move:
    prv_r, prv_c=cur_r, cur_c
    cur_r+=move_r[mv]
    cur_c+=move_c[mv]
    if cur_r<0 or cur_c<0 or cur_r>=m or cur_c>=m+n-1:
        print(1, strings[prv_r][prv_c]) 
        letters+=strings[prv_r][prv_c]
        cur_r, cur_c=prv_r, prv_c
    elif strings[cur_r][cur_c]==" ": 
        print(2, strings[prv_r][prv_c])
        letters+=strings[prv_r][prv_c]
        cur_r, cur_c=prv_r, prv_c
    else: letters+=strings[cur_r][cur_c]
print(letters, len(set(letters)), sep="\n")