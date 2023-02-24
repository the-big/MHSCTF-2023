This is a maximum weight matching problem. So using a python package we can do this very easily.


```python
import socket
import numpy
import time
import random
import networkx as nx

def solve():

    k = open("in0").read()

    k = k.split("\n")[:-1]

    for a in range(len(k)):
        k[a] = k[a].split(" ")

    for a in range(len(k)):
        for b in range(len(k[a])):
            k[a][b] = int(k[a][b])

    for a in range(len(k)):
        k[a].insert(a, -1)

    pairs = []

    for a in range(len(k)):
        for b in range(a + 1, len(k)):
            pairs.append((a, b, k[a][b] + k[b][a]))

    G = nx.Graph()
    G.add_weighted_edges_from(pairs)
    sol = sorted(nx.max_weight_matching(G))
    print(sol)

    ans = ""

    for i in range(len(sol)):
        ans += (
            str(sol[i][0])
            + ","
            + str(sol[i][1])
            + ";"
            + str(sol[i][1])
            + ","
            + str(sol[i][0])
            + ";"
        )

    ans = ans[:-1]
    print(ans)
    return ans

    # for i in range(3):

solve()

# s = socket.socket()
# s.connect(("0.cloud.chals.io", 22304))
# for i in range(3):
#     print(i)
#     time.sleep(3)
#     recv = s.recv(1 << 30).decode()
#     print(recv)
#     open("in" + str(i), "w").write(recv)
#     time.sleep(3)
#     sol = solve(recv)
#     print(sol)
#     open("out" + str(i), "w").write(sol)
#     s.send(sol.encode())
# recv = s.recv(1 << 30).decode()
# print(recv)
```

    
`valentine{l0V3_i5_1n_7he_4ir}`
