
To solve this we can get the 4 numbers (people) that will try to match with us. To do this we will use the decrypt function in bfv (see code). We will go through all numbers of a secret key and once we decrypt and encrypt and get the same output we know that is a working secret key.

<details>
  <summary> Code </summary>
  
  ```python
  import base64
  import bfv
  import pickle
  import pwn
  import random
  import numpy as np
  from typing import Any

  def prod(a: list[bfv.Ctxt]) -> bfv.Ctxt:
      if len(a) == 1:
          return a[0]
      mid = len(a) // 2
      return prod(a[:mid]) * prod(a[mid:])

  def check_elem(needle: bfv.Ctxt, haystack: list[bfv.Ctxt]):
      diffs = [h - needle for h in haystack]
      r = needle.ctx.encrypt(random.randint(1, needle.ctx.ptxt_mod - 1))
      return r * prod(diffs)

  def recv_context(conn: pwn.remote):
      data = conn.recvline()
      return bfv.Context.from_json(base64.b64decode(data))

  def recv_ctxts(conn: pwn.remote):
      data = conn.recvline()
      return [
          bfv.Ctxt.from_json(base64.b64decode(piece).decode("utf-8"))
          for piece in data.decode("utf-8").split(";;")
      ]

  def send_ctxts(conn: pwn.remote, data: list[bfv.Ctxt]):
      raw = [
          base64.b64encode(bytes(ctxt.to_json(), "utf-8")).decode("utf-8")
          for ctxt in data
      ]
      conn.sendline(";;".join(raw).encode("utf-8"))

  def one_round(conn: pwn.remote):
      context = recv_context(conn)
      their_set = recv_ctxts(conn)

      # print(context)
      # print(context.pk[0](1) % 7, context.pk[0](2) % 7)
      # for i in context.rlks:
      #     print(i[0](1) % 7, i[0](2) % 7)
      print(their_set)

      while True:
          my_set_inp = input("Enter four numbers: ").split()
          my_set_inp_enc = [context.encrypt(int(x)) for x in my_set_inp]
          sk = 0
          for secret in range(100):
              num = 0
              for j in range(4):
                  if int(my_set_inp_enc[j].decrypt(bfv.np.poly1d(secret))(0)) == int(
                      my_set_inp[j]
                  ):
                      num += 1
              if num == 4:
                  sk = secret
                  break
              print("secret:", secret, num)
          print(sk)
          their_set_dec = [ctxt.decrypt(bfv.np.poly1d(sk)) for ctxt in their_set]
          print(their_set_dec)
          my_set_inp = input("Enter four numbers: ").split()
          break

      my_set = list(map(int, my_set_inp))
      my_set_enc = [context.encrypt(x) for x in my_set]

      print(my_set_enc)

      results: list[bfv.Ctxt] = []
      for needle in their_set:
          results.append(check_elem(needle, my_set_enc))

      send_ctxts(conn, results)

  host = "0.cloud.chals.io"
  port = 29661

  with pwn.remote(host, port) as s:
      instructions = s.recvline()
      print(instructions.decode("utf-8"))

      for _ in range(10):
          one_round(s)
          print(result := s.recvline().decode("utf-8"))
          if not result.startswith("You"):
              break
      else:
          flag = s.recvline().decode("utf-8")
          print(f"flag: {flag}")
  ```
</details>

When running client.py first type 4 random numbers (e.g. 0 0 0 0). This will give 4 numbers. These 4 numbers will be the numbers that will try to date with us. And since Alex is the smallest one type the number that is the smallest 4 times (e.g. 0 0 0 0).

`valentine{my_b1g_fr13nd1y_v4l3nt1n3}`
