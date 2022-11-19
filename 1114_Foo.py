from threading import Barrier

class Foo:
    def __init__(self):
        self.first_barrier = Barrier(parties=2)
        self.second_barrier = Barrier(parties=2)

    def first(self, printFirst: 'Callable[[], None]') -> None:    
        printFirst()
        self.first_barrier.wait()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_barrier.wait()
        printSecond()
        self.second_barrier.wait()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_barrier.wait()
        printThird()
        
# Alternative solution

from threading import Lock

class Foo:
    def __init__(self):
        self.locks = [Lock(), Lock()]
        self.locks[0].acquire()
        self.locks[1].acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:    
        printFirst()
        self.locks[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.locks[0]:
            printSecond()
            self.locks[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.locks[1]:
            printThird()
            
# Alternative solution

from threading import Event

class Foo:
    def __init__(self):
        self.done1, self.done2 = (Event(), Event())

    def first(self, printFirst: 'Callable[[], None]') -> None:    
        printFirst()
        self.done1.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.done1.wait()
        printSecond()
        self.done2.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.done2.wait()
        printThird()
        
# Alternative solution

from threading import Semaphore

class Foo:
    def __init__(self):
        self.gates = (Semaphore(0), Semaphore(0))

    def first(self, printFirst: 'Callable[[], None]') -> None:    
        printFirst()
        self.gates[0].release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.gates[0]:
            printSecond()
            self.gates[1].release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.gates[1]:
            printThird()
            
# Alternative solution

from threading import Condition

class Foo:
    def __init__(self):
        self.condition = Condition()
        self.order = 0
        self.first_finished = lambda: self.order == 1
        self.second_finished = lambda: self.order == 2

    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self.condition:
            printFirst()
            self.order = 1
            self.condition.notify(2)

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.condition:
            self.condition.wait_for(self.first_finished)
            printSecond()
            self.order = 2
            self.condition.notify(1)

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.condition:
            self.condition.wait_for(self.second_finished)
            printThird()
