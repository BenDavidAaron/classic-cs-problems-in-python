from typing import Generator

def fib(n: int) -> Generator[int, None, None]:
    if n == 0: return n
    lst: int = 0
    nxt: int = 1
    for _ in range(1,n):
        lst, nxt = nxt, lst + nxt
        yield nxt

if __name__ == "__main__":
    for i in fib(50):
        print(i)