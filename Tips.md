## standard input 

```py
a, b = map(int, input.split())
a, b, c, x = [int(input()) for i in range(4)]
A = list(map(int, input().split()))
## 縦にくるタイプ
n = input()
ary = []
[ary.append(int(input())) for i in range(int(n))]
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