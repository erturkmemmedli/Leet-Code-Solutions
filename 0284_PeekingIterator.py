# Below is the interface for Iterator, which is already defined for you.
# class Iterator:
#     def __init__(self, nums):
#         # Initializes an iterator object to the beginning of a list.
#     def hasNext(self):
#         #Returns true if the iteration has more elements.
#     def next(self):
#         # Returns the next element in the iteration.

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        if self.iterator.hasNext():
            self.next_value = self.iterator.next()
        else:
            self.next_value = None

    def peek(self):
        return self.next_value

    def next(self):
        temp = self.next_value
        if self.iterator.hasNext():
            self.next_value = self.iterator.next()
        else:
            self.next_value = None
        return temp

    def hasNext(self):
        return bool(self.next_value)

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
