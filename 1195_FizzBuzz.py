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
