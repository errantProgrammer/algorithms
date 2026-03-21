"""
src: https://www.codewars.com/kata/556deca17c58da83c00002db
"""


def tribonacci(signature, n):
    if n == 0:
        return []
    if n == 1:
        return [signature[0]]
    if n == 2:
        return [signature[0], signature[1]]
    sol = signature[:]  # copy of signature
    for i in range(n - 3):
        sol.append(sum(sol[i : i + 3]))
    return sol


"""
Other solution
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
"""
