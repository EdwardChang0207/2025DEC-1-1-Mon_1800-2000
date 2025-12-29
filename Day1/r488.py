r, c, d=map(int, input().split())
board=[[d]*c for _ in range(r)]
k=int(input())
dinos=[[0]*c for _ in range(r)]
for i in range(k):
    ri, ci=map(int, input().split())
    dinos[ri][ci]+=1
m=int(input())
for j in range(m):
    aj, bj, sj, dj=map(int, input().split())
    flag=False
    for x in range(bj-sj//2, bj+sj//2+1):
        for y in range(aj-sj//2, aj+sj//2+1):
            if x>=0 and x<c and y>=0 and y<r:
                if dinos[y][x]: 
                    dinos[y][x]=0
                    flag=True
    if not flag:
        for y in range(bj-sj//2, bj+sj//2+1):
            for x in range(aj-sj//2, aj+sj//2+1):
                if x>=0 and x<c and y>=0 and y<r: board[y][x]-=dj

maxi, mini=-1000, 101
for a in range(len(board)):
    if max(board[a])>maxi: maxi=max(board[a])
    if min(board[a])<mini: mini=min(board[a])
ans=0
for b in range(len(dinos)):
    ans+=sum(dinos[b])
print(maxi, mini, ans)
