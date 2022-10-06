from threading import Barrier, Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.barrier = [Barrier(2), Barrier(2)]
        self.lock = Lock()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.lock.acquire()
            printNumber(0)
            self.count += 1
            self.barrier[self.count % 2].wait()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2):
            self.barrier[0].wait()
            printNumber(self.count)
            self.lock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n + 1) // 2):
            self.barrier[1].wait()
            printNumber(self.count)
            self.lock.release()
            
# Alternative solution

from threading import Lock

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.lock = [Lock(), Lock(), Lock()]
        self.lock[0].acquire()
        self.lock[1].acquire()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.lock[2].acquire()
            printNumber(0)
            self.count += 1
            self.lock[self.count % 2].release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2):
            self.lock[0].acquire()
            printNumber(self.count)
            self.lock[2].release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n + 1) // 2):
            self.lock[1].acquire()
            printNumber(self.count)
            self.lock[2].release()
            
# Alternative solution

from threading import Semaphore

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.semaphore = [Semaphore(), Semaphore(), Semaphore()]
        self.semaphore[0].acquire()
        self.semaphore[1].acquire()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.semaphore[2].acquire()
            printNumber(0)
            self.count += 1
            self.semaphore[self.count % 2].release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2):
            self.semaphore[0].acquire()
            printNumber(self.count)
            self.semaphore[2].release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n + 1) // 2):
            self.semaphore[1].acquire()
            printNumber(self.count)
            self.semaphore[2].release()
            
# Alternative solution

from threading import Event

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.event = [Event(), Event(), Event()]
        self.event[2].set()
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.event[2].wait()
            self.event[2].clear()
            printNumber(0)
            self.count += 1
            self.event[self.count % 2].set()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2):
            self.event[0].wait()
            self.event[0].clear()
            printNumber(self.count)
            self.event[2].set()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n + 1) // 2):
            self.event[1].wait()
            self.event[1].clear()
            printNumber(self.count)
            self.event[2].set()
            
# Alternative solution

from threading import Condition

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.condition = Condition()
        self.order = 2
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda: self.order == 2)
                printNumber(0)
                self.count += 1
                self.order = self.count % 2
                self.condition.notify(2)
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2):
            with self.condition:
                self.condition.wait_for(lambda: self.order == 0)
                printNumber(self.count)
                self.order = 2
                self.condition.notify(2)

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n + 1) // 2):
            with self.condition:
                self.condition.wait_for(lambda: self.order == 1)
                printNumber(self.count)
                self.order = 2
                self.condition.notify(2)
