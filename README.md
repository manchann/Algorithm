# Algorithm
알고리즘 문제를 풀고 커밋

### 목표
- python으로 알고리즘 문제 풀이 실력 증가

### Python Input 처리
- 한줄, 공백 처리, 데이터의 갯수가 정해져 있을 경우
```
N, M = map(int, input().split())
```

- 1차원 배열로 입력받기
```
arr = list(map(int, input().split()) 
```

- N행으로 이루어진 2차원 배열 입력
```
N = int(input()) # 행렬의 크기

arr = [list(map(int, input().split())) for _ in range(N)]
```
