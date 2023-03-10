from threading import Lock

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.Fizz = Lock()
        self.Buzz = Lock()
        self.FizzBuzz = Lock()
        self.Number = Lock()
        self.Fizz.acquire()
        self.Buzz.acquire()
        self.FizzBuzz.acquire()
        
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.Fizz.acquire()
            if self.n == 0: return
            printFizz()
            self.Number.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.Buzz.acquire()
            if self.n == 0: return
            printBuzz()
            self.Number.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.FizzBuzz.acquire()
            if self.n == 0: return
            printFizzBuzz()
            self.Number.release()     

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.Number.acquire()
            if i % 15 == 0:
                self.FizzBuzz.release()
            elif i % 5 == 0:
                self.Buzz.release()
            elif i % 3 == 0:
                self.Fizz.release()
            else:
                printNumber(i)
                self.Number.release()     
        self.Number.acquire()
        self.n = 0
        self.Fizz.release()
        self.Buzz.release()
        self.FizzBuzz.release()
        return

# Alternative solution

from threading import Semaphore

class FizzBuzz1:
    def __init__(self, n: int):
        self.n = n
        self.Fizz = Semaphore(0)
        self.Buzz = Semaphore(0)
        self.FizzBuzz = Semaphore(0)
        self.Number = Semaphore(1)
        self.done = False
        
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        while True:
            self.Fizz.acquire()
            if self.done: return
            printFizz()
            self.Number.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        while True:
            self.Buzz.acquire()
            if  self.done: return
            printBuzz()
            self.Number.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        while True:
            self.FizzBuzz.acquire()
            if  self.done: return
            printFizzBuzz()
            self.Number.release()     

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.Number.acquire()
            if i % 15 == 0:
                self.FizzBuzz.release()
            elif i % 5 == 0:
                self.Buzz.release()
            elif i % 3 == 0:
                self.Fizz.release()
            else:
                printNumber(i)
                self.Number.release()     
        self.Number.acquire()
        self.done = True
        self.Fizz.release()
        self.Buzz.release()
        self.FizzBuzz.release()
        return
    
# Alternative solution

from threading import Barrier

class FizzBuzz2:
    def __init__(self, n: int):
        self.n = n
        self.barrier = Barrier(4)
        
    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 != 0:
                printFizz()
            self.barrier.wait()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 == 0:
                printBuzz()
            self.barrier.wait()
            
    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 == 0 and i % 5 == 0:
                printFizzBuzz()
            self.barrier.wait()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 3 != 0 and i % 5 != 0:
                printNumber(i)
            self.barrier.wait()
