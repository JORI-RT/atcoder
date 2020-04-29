- [standard input](#anchor1")
    - [通常の入力](#通常の入力)
    - [縦タイプ](#縦タイプ)
    - [slice](#slice)
    - [curry](#curry)
## standard input 

<a id="anchor1"></a>

### 通常の入力
```py
a, b = map(int, input().split())
a, b, c, x = [int(input()) for i in range(4)]
```
### 縦タイプ
```sh
# input
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

## 平方根
```py
import math 

math.sqrt(x)
```

## curry 

```python
from functools import reduce
from operator import add
from operator import sub
from operator import mul

array = [20, 1, 2, 3, 4, 5]

print(reduce(add, array)) # 35
print(reduce(sub, array)) # 5
print(reduce(mul, array)) # 2400
```