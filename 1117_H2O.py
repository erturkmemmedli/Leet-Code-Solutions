from threading import Lock

class H2O:
    def __init__(self):
        self.locks = [Lock(), Lock()]
        self.locks[1].acquire()
        self.count = 0

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.locks[0].acquire()
        releaseHydrogen()
        self.count += 1
        if self.count % 2 == 0:
            self.locks[1].release()
        else:
            self.locks[0].release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        # releaseOxygen() outputs "O". Do not change or remove this line.
        self.locks[1].acquire()
        releaseOxygen()
        self.locks[0].release()
        
# Alternative solution

from threading import Barrier, Semaphore

class H2O:
    def __init__(self):
        self.barrier = Barrier(3)
        self.H = Semaphore(2)
        self.O = Semaphore(1)

    def hydrogen(self, releaseHydrogen) -> None:
        self.H.acquire()
        self.barrier.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.H.release()

    def oxygen(self, releaseOxygen) -> None:
        self.O.acquire()
        self.barrier.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.O.release()
