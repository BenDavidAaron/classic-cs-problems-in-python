def fib(n: int) -> int:
    if n == 0: return n
    lst: int = 0
    nxt: int = 1
    for _ in range(1,n):
        lst, nxt = nxt, lst + nxt
    return nxt

if __name__ == "__main__":
    print(fib(1))
    print(fib(10))
    print(fib(20))
    print(fib(30))