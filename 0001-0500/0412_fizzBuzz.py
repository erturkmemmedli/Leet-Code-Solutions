class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzbuzz = []
        for i in range(n):
            if (i+1) % 15 == 0:
                fizzbuzz.append('FizzBuzz')
            elif (i+1) % 3 == 0:
                fizzbuzz.append('Fizz')
            elif (i+1) % 5 == 0:
                fizzbuzz.append('Buzz')
            else:
                fizzbuzz.append(str(i+1))
        return fizzbuzz
