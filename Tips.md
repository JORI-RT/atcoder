## standard input 

```py
a, b = map(int, input.split())
a, b, c, x = [int(input()) for i in range(4)]
```
### 縦タイプ
```sh
# 縦タイプ
3
1 1
2 4
4 3
# 
N = int(input())
d = [list(map(int, input().split())) for _ in range(N)]
```

## slice
```py
a = [1, 2, 3, 4, 5]
print(a[:: 2])
print(a[1:: 2])
print(a[::-1])
print(a[1::-1])

>>>
[1, 3, 5]
[2, 4]
[5, 4, 3, 2, 1]
[2, 1]
```