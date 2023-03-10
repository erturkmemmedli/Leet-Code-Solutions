from threading import Barrier

class FooBar:
    def __init__(self, n):
        self.n = n
        self.barrier = Barrier(2)
    
    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.barrier.wait()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.barrier.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            
# Alternative solution

from threading import Condition

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_counter = 0
        self.bar_counter = 0
        self.condition = Condition()
    
    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda: self.foo_counter == self.bar_counter)
                printFoo()
                self.foo_counter += 1
                self.condition.notify(1)

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda: self.foo_counter > self.bar_counter)
                printBar()
                self.bar_counter += 1
                self.condition.notify(1)
                
# Alternative solution

from threading import Event

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_print = Event()
        self.bar_print = Event()
        self.bar_print.set()
    
    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_print.wait()
            self.bar_print.clear()
            printFoo()
            self.foo_print.set()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_print.wait()
            self.foo_print.clear()
            printBar()
            self.bar_print.set()
            
# Alternative solution

from threading import Lock

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()
    
    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()
            
# Alternative solution

from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_gate = Semaphore(1)
        self.bar_gate = Semaphore(0)
    
    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.foo_gate.acquire()
            printFoo()
            self.bar_gate.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.bar_gate.acquire()
            printBar()
            self.foo_gate.release()
