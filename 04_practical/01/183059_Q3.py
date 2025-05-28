from typing import None

def countdown(n: int) -> None:
    if n < 0:
        return
    countdown(n - 1)
    print(n)
