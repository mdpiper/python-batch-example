#! /usr/bin/env python
import time


class Example:

    def __init__(self) -> None:
        self.value = 0
        self.n_iter = 600

    def compute(self) -> None:
        self.value += 1


if __name__ == "__main__":
    print("Start")

    e = Example()
    for i in range(e.n_iter):
        time.sleep(0.1)
        e.compute()
        if i % 10 == 0:
            print(i, e.value)

    print("Finish")
