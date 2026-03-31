from collections import deque

def wall():

    q=deque()
    q.append((0,0,0))
    visited[0][0][0] = 1

    while q:
        nowi, nowj, nowk = q.popleft()

        if nowi == N-1 and nowj == M-1:
            return visited[nowi][nowj][nowk]
        
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni = nowi + di
            nj = nowj + dj

            if 0 <= ni < N and 0 <= nj < M:
                
                if arr[ni][nj] == 1 and nowk < K and visited[ni][nj][nowk+1] == 0:
                    visited[ni][nj][nowk+1] = visited[nowi][nowj][nowk]+1
                    q.append((ni,nj,nowk+1))
                elif arr[ni][nj] == 0 and visited[ni][nj][nowk] == 0:
                    visited[ni][nj][nowk] = visited[nowi][nowj][nowk]+1
                    q.append((ni,nj,nowk))

    return  -1

N,M,K = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]

print(wall())