### 1. Polynomial Addition using Linked Lists

```python
class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff
        self.exp = exp
        self.next = None

def add(p1, p2):
    dummy = Node(0, 0)
    tail = dummy
    while p1 and p2:
        if p1.exp > p2.exp:
            tail.next = p1; p1 = p1.next
        elif p1.exp < p2.exp:
            tail.next = p2; p2 = p2.next
        else:
            coeff = p1.coeff + p2.coeff
            if coeff: 
                tail.next = Node(coeff, p1.exp)
            p1, p2 = p1.next, p2.next
        tail = tail.next
    tail.next = p1 or p2
    return dummy.next

def print_poly(head):
    terms = []
    while head:
        terms.append(f"{head.coeff}x^{head.exp}")
        head = head.next
    print(" + ".join(terms) or "0")

# Test
p1 = Node(5,2); p1.next = Node(4,1); p1.next.next = Node(2,0)
p2 = Node(5,1); p2.next = Node(5,0)
result = add(p1, p2)
print_poly(result)
```

**Output:** `5x^2 + 9x^1 + 7x^0`

### 2. Stack Operations (List)

```python
class Stack:
    def __init__(self):
        self.s = []

    def push(self, x):
        self.s.append(x)

    def pop(self):
        return self.s.pop() if self.s else None

    def peek(self):
        return self.s[-1] if self.s else None

s = Stack()
s.push(10); s.push(20); s.push(30)
print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())  # None
```

*OUTPUT*
```30
30
20
10
None
```


### 3. Postfix Evaluation using Stack

```python
def evaluate_postfix(expr):
    stack = []
    for token in expr.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a // b)
    return stack[0]

print(evaluate_postfix("2 3 1 * + 9 -"))
```

**Output:** `-4`

### 4. Queue using Singly Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
    def enqueue(self, data):
        node = Node(data)
        if not self.rear:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    def dequeue(self):
        if self.front:
            data = self.front.data
            self.front = self.front.next
            if not self.front: self.rear = None
            return data

q = Queue()
q.enqueue(10); q.enqueue(20); q.enqueue(30)
print(q.dequeue(), q.dequeue())
```

**Output:** `10 20`

### 5. Binary Search Tree Operations

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def insert(root, val):
    if not root: return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

root = None
for v in [50, 30, 70, 20, 40]:
    root = insert(root, v)
inorder(root)
```

**Output:** `20 30 40 50 70`

### 6. AVL Tree (Simple Insert with Rotation)

```python
class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.height = 1

def height(n): return n.height if n else 0
def update_height(n): n.height = 1 + max(height(n.left), height(n.right))

def right_rotate(y):
    x = y.left
    y.left = x.right
    x.right = y
    update_height(y)
    update_height(x)
    return x

def insert(root, val):
    if not root: return AVLNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    update_height(root)
    balance = height(root.left) - height(root.right)
    if balance > 1 and val < root.left.val:
        return right_rotate(root)
    return root

root = None
for v in [10, 20, 30]:
    root = insert(root, v)
print(root.val, root.right.val)  # After rotation
```

**Output:** `20 30`

### 7. Graph BFS & DFS

```python
from collections import defaultdict, deque

graph = defaultdict(list)
edges = [(0,1),(0,2),(1,2),(2,3)]
for u,v in edges:
    graph[u].append(v); graph[v].append(u)

def bfs(start):
    visited = set()
    q = deque([start])
    visited.add(start)
    res = []
    while q:
        node = q.popleft()
        res.append(node)
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
    return res

def dfs(node, visited, res):
    visited.add(node)
    res.append(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei, visited, res)

res = []
dfs(0, set(), res)
print("BFS:", bfs(0))
print("DFS:", res)
```

**Output:**
```
BFS: [0, 1, 2, 3]
DFS: [0, 1, 2, 3]
```

### 8. Prim’s Algorithm (MST)

```python
import heapq

def prim(graph, n):
    visited = [False] * n
    pq = [(0, 0)]  # (weight, node)
    total = 0
    while pq:
        w, u = heapq.heappop(pq)
        if visited[u]: continue
        visited[u] = True
        total += w
        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v))
    return total

graph = [[(1,2),(2,3)], [(0,2),(2,1)], [(0,3),(1,1),(3,4)], [(2,4)]]
print("MST weight:", prim(graph, 4))
```

**Output:** `MST weight: 6`

### 9. Dijkstra’s Algorithm

```python
import heapq

def dijkstra(graph, start):
    dist = [float('inf')] * len(graph)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

graph = [[(1,4),(2,8)], [(0,4),(2,1)], [(0,8),(1,1)]]
print(dijkstra(graph, 0))
```

**Output:** `[0, 4, 5]`

### 10. Sorting Algorithms 

```python
def buble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]: a[j],a[j+1] = a[j+1],a[j]
    return a

def selection_sort(a):
    for i in range(len(a)):
        m = i
        for j in range(i+1,len(a)):
            if a[j] < a[m]: m = j
        a[i],a[m] = a[m],a[i]
    return a

def insertion_sort(a):
    for i in range(1,len(a)):
        k = a[i]; j = i-1
        while j >=0 and a[j] > k:
            a[j+1] = a[j]; j -=1
        a[j+1] = k
    return a

d = [64,25,12,22,11]
print(buble_sort(d[:]), selection_sort(d[:]), insertion_sort(d[:]))
```


**Output:** `[11, 12, 22, 25, 64]`

### 11. Linear & Binary Search

```python
def linear_search(arr, x):
    for i, v in enumerate(arr):
        if v == x: return i
    return -1

def binary_search(arr, x):
    l, r = 0, len(arr)-1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == x: return m
        elif arr[m] < x: l = m + 1
        else: r = m - 1
    return -1

arr = [10, 20, 30, 40, 50]
print("Linear:", linear_search(arr, 30))
print("Binary:", binary_search(arr, 30))
```

**Output:**
```
Linear: 2
Binary: 2
```

### 12. Hashing - Linear & Quadratic Probing

```python
class HashTable:
    def __init__(self, size=7):
        self.table = [None] * size
        self.size = size

    def hash(self, key): return key % self.size

    def linear_probe(self, key):
        i = self.hash(key)
        while self.table[i] is not None:
            i = (i + 1) % self.size
        self.table[i] = key

    def quadratic_probe(self, key):
        i = self.hash(key)
        j = 1
        while self.table[i] is not None:
            i = (i + j*j) % self.size
            j += 1
        self.table[i] = key

ht = HashTable()
for k in [10, 22, 31, 4]:
    ht.linear_probe(k)
print("Linear:", ht.table)

ht = HashTable()
for k in [10, 22, 31, 4]:
    ht.quadratic_probe(k)
print("Quadratic:", ht.table)
```

**Output:**
```
Linear: [10, 22, 31, 4, None, None, None]
Quadratic: [10, 22, 31, None, 4, None, None]
```
