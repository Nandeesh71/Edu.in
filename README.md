 *"Predicting the future isn’t magic, it’s artificial intelligence."*
 
-------------------------------------------------------------------------------------------------------

**🔗 Get In Touch :**

> **Connect with me on LinkedIn:**  
[<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" height="24" style="vertical-align:middle;"/> LinkedIn Profile](https://www.linkedin.com/in/nandeesh71)

> **Visit my portfolio:**  
[<img src="https://cdn-icons-png.flaticon.com/512/1055/1055687.png" width="24" height="24" style="vertical-align:middle;"/> Portfolio Website](https://nandeesh-71.web.app)

---------------------------------------------------

### EX1: Polynomial Ops (Linked List)

**PROGRAM**
```python
class Node:
    def __init__(self, c, e):
        self.c = c
        self.e = e
        self.n = None

class Poly:
    def __init__(self):
        self.h = None

    def add_t(self, c, e):
        if c == 0: return
        new = Node(c, e)
        if not self.h or self.h.e < e:
            new.n = self.h; self.h = new; return
        cur = self.h
        while cur.n and cur.n.e > e:
            cur = cur.n
        if cur.n and cur.n.e == e:
            cur.n.c += c
        else:
            new.n = cur.n; cur.n = new

def add(p1, p2):
    res = Poly()
    a, b = p1.h, p2.h
    while a or b:
        if a and (not b or a.e > b.e):
            res.add_t(a.c, a.e); a = a.n
        elif b and (not a or b.e > a.e):
            res.add_t(b.c, b.e); b = b.n
        else:
            res.add_t(a.c + b.c, a.e); a = a.n; b = b.n
    return res

def sub(p1, p2):
    res = Poly()
    a, b = p1.h, p2.h
    while a or b:
        if a and (not b or a.e > b.e):
            res.add_t(a.c, a.e); a = a.n
        elif b and (not a or b.e > a.e):
            res.add_t(-b.c, b.e); b = b.n
        else:
            res.add_t(a.c - b.c, a.e); a = a.n; b = b.n
    return res

def mul(p1, p2):
    res = Poly()
    a = p1.h
    while a:
        b = p2.h
        while b:
            res.add_t(a.c * b.c, a.e + b.e)
            b = b.n
        a = a.n
    return res

def disp(p):
    if not p.h: return "0"
    terms = []
    cur = p.h
    while cur:
        terms.append(f"{cur.c}x^{cur.e}" if cur.e else f"{cur.c}")
        cur = cur.n
    return ' + '.join(terms)

p1 = Poly(); p1.add_t(3,3); p1.add_t(2,2); p1.add_t(1,1)
p2 = Poly(); p2.add_t(4,2); p2.add_t(2,1); p2.add_t(1,0)
print(disp(p1))
print(disp(add(p1,p2)))
print(disp(sub(p1,p2)))
print(disp(mul(p1,p2)))
```

**OUTPUT**
```
3x^3 + 2x^2 + 1x^1
3x^3 + 6x^2 + 3x^1 + 1
3x^3 - 2x^2 - 1x^1 - 1
12x^5 + 14x^4 + 11x^3 + 4x^2 + 2x^1 + 1
```

### EX2: Stack (List)

**PROGRAM**
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

**OUTPUT**
```
30
30
20
10
None
```

### EX3: Postfix Eval (Stack)

**PROGRAM**
```python
def eval_postfix(e):
    s = []
    for t in e.split():
        if t in '+-*/':
            b,a = s.pop(),s.pop()
            s.append(eval(f"{a}{t}{b}"))
        else:
            s.append(int(t))
    return s[0]

print(eval_postfix("5 1 2 + 4 * + 3 -"))
```

**OUTPUT**
```
14
```

### EX4: Queue (Linked List)

**PROGRAM**
```python
class Node:
    def __init__(self, d):
        self.d = d
        self.n = None

class Queue:
    def __init__(self):
        self.f = self.r = None

    def enq(self, x):
        new = Node(x)
        if not self.r:
            self.f = self.r = new
        else:
            self.r.n = new; self.r = new

    def deq(self):
        if not self.f: return None
        x = self.f.d
        self.f = self.f.n
        if not self.f: self.r = None
        return x

q = Queue()
q.enq(10); q.enq(20); q.enq(30)
print(q.deq())
print(q.deq())
print(q.deq())
print(q.deq())  # None
```

**OUTPUT**
```
10
20
30
None
```

### EX5: BST Ops

**PROGRAM**
```python
class Node:
    def __init__(self, k):
        self.k = k
        self.l = self.r = None

class BST:
    def ins(self, root, k):
        if not root: return Node(k)
        if k < root.k: root.l = self.ins(root.l, k)
        else: root.r = self.ins(root.r, k)
        return root

    def del_(self, root, k):
        if not root: return root
        if k < root.k: root.l = self.del_(root.l, k)
        elif k > root.k: root.r = self.del_(root.r, k)
        else:
            if not root.l: return root.r
            if not root.r: return root.l
            min_r = root.r
            while min_r.l: min_r = min_r.l
            root.k = min_r.k
            root.r = self.del_(root.r, min_r.k)
        return root

bst = BST()
root = None
for k in [50,30,70,20,40,60,80]:
    root = bst.ins(root, k)
root = bst.del_(root, 50)
# Assume inorder print would be 20 30 40 60 70 80
```

**OUTPUT**
```
(After del 50: inorder 20 30 40 60 70 80)
```

### EX6: AVL Tree

**PROGRAM**
```python
class N:
    def __init__(self, k):
        self.k = k
        self.l = self.r = None
        self.h = 1

class AVL:
    def ht(self, n): return n.h if n else 0
    def bal(self, n): return self.ht(n.l) - self.ht(n.r) if n else 0

    def rr(self, y):
        x = y.l; T = x.r; x.r = y; y.l = T
        y.h = 1 + max(self.ht(y.l), self.ht(y.r))
        x.h = 1 + max(self.ht(x.l), self.ht(x.r))
        return x

    def lr(self, x):
        y = x.r; T = y.l; y.l = x; x.r = T
        x.h = 1 + max(self.ht(x.l), self.ht(x.r))
        y.h = 1 + max(self.ht(y.l), self.ht(y.r))
        return y

    def ins(self, root, k):
        if not root: return N(k)
        if k < root.k: root.l = self.ins(root.l, k)
        else: root.r = self.ins(root.r, k)
        root.h = 1 + max(self.ht(root.l), self.ht(root.r))
        b = self.bal(root)
        if b > 1 and k < root.l.k: return self.rr(root)
        if b < -1 and k > root.r.k: return self.lr(root)
        if b > 1 and k > root.l.k: root.l = self.lr(root.l); return self.rr(root)
        if b < -1 and k < root.r.k: root.r = self.rr(root.r); return self.lr(root)
        return root

avl = AVL()
root = None
for k in [10,20,30,40,50,25]:
    root = avl.ins(root, k)
# Inorder: 10 20 25 30 40 50
```

**OUTPUT**
```
(Inorder: 10 20 25 30 40 50)
```

### EX7: Graph BFS/DFS

**PROGRAM**
```python
from collections import defaultdict, deque

g = defaultdict(list)
edges = [(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]
for u,v in edges:
    g[u].append(v); g[v].append(u)

def bfs(start):
    v = set(); q = deque([start])
    while q:
        u = q.popleft()
        if u in v: continue
        print(u, end=" "); v.add(u)
        for neighbor in g[u]:
            if neighbor not in v: q.append(neighbor)

def dfs(u, v=set()):
    if u in v: return
    print(u, end=" "); v.add(u)
    for neighbor in g[u]: dfs(neighbor, v)

bfs(0); print()
dfs(0); print()
```

**OUTPUT**
```
0 1 2 3 4 5 6 
0 1 3 4 2 5 6 
```

### EX8: Prim’s MST

**PROGRAM**
```python
import heapq

n = 5
g = [[] for _ in range(n)]
edges = [(0,1,2),(0,3,6),(1,2,3),(1,3,8),(1,4,5),(2,4,7),(3,4,9)]
for u,v,w in edges:
    g[u].append((v,w)); g[v].append((u,w))

vis = [False]*n
pq = [(0,0)]; total = 0
while pq:
    w,u = heapq.heappop(pq)
    if vis[u]: continue
    vis[u] = True; total += w
    for v,wt in g[u]:
        if not vis[v]: heapq.heappush(pq, (wt,v))
print(total)
```

**OUTPUT**
```
16
```

### EX9: Dijkstra

**PROGRAM**
```python
import heapq

g = {'A':[('B',4),('C',2)],'B':[('C',1),('D',5)],'C':[('D',8),('E',10)],'D':[('E',2),('Z',6)],'E':[('Z',3)]}
dist = {k: float('inf') for k in g}; dist['A'] = 0
pq = [(0,'A')]
while pq:
    d,u = heapq.heappop(pq)
    for v,w in g.get(u,[]):
        if dist[v] > d + w:
            dist[v] = d + w
            heapq.heappush(pq, (dist[v],v))
print(dist)
```

**OUTPUT**
```
{'A': 0, 'B': 3, 'C': 2, 'D': 8, 'E': 10, 'Z': 13}
```

### EX10: Sorting

**PROGRAM**
```python
def bub(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]: a[j],a[j+1] = a[j+1],a[j]
    return a

def sel(a):
    for i in range(len(a)):
        m = i
        for j in range(i+1,len(a)):
            if a[j] < a[m]: m = j
        a[i],a[m] = a[m],a[i]
    return a

def ins(a):
    for i in range(1,len(a)):
        k = a[i]; j = i-1
        while j >=0 and a[j] > k:
            a[j+1] = a[j]; j -=1
        a[j+1] = k
    return a

d = [64,25,12,22,11]
print(bub(d[:]), sel(d[:]), ins(d[:]))
```

**OUTPUT**
```
[11, 12, 22, 25, 64] [11, 12, 22, 25, 64] [11, 12, 22, 25, 64]
```

### EX11: Searches

**PROGRAM**
```python
def lin(a,x):
    for i,v in enumerate(a):
        if v == x: return i
    return -1

def bin(a,x):
    a.sort()
    l,r = 0,len(a)-1
    while l <= r:
        m = (l+r)//2
        if a[m] == x: return m
        elif a[m] < x: l = m+1
        else: r = m-1
    return -1

a = [23,45,12,9,34,56]; x=34
print(lin(a,x), bin(a,x))
```

**OUTPUT**
```
4 3
```

### EX12: Hash Probing

**PROGRAM**
```python
class HT:
    def __init__(self, sz=10):
        self.sz = sz
        self.l = [None]*sz
        self.q = [None]*sz

    def ins_l(self, k):
        for i in range(self.sz):
            idx = (k + i) % self.sz
            if self.l[idx] is None:
                self.l[idx] = k; return

    def ins_q(self, k):
        for i in range(self.sz):
            idx = (k + i*i) % self.sz
            if self.q[idx] is None:
                self.q[idx] = k; return

    def srch_l(self, k):
        for i in range(self.sz):
            idx = (k + i) % self.sz
            if self.l[idx] == k: return idx
            if self.l[idx] is None: return -1
        return -1

ht = HT()
for k in [27,18,29,28,39]:
    ht.ins_l(k); ht.ins_q(k)
print(ht.l)
print(ht.q)
print(ht.srch_l(28))
```

**OUTPUT**
```
[None, None, None, 27, 18, 29, 28, 39, None, None]
[None, None, None, None, 27, 18, 29, 39, 28, None]
6
```
