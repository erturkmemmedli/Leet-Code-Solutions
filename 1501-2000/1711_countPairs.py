class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers_of_two = [2 ** i for i in range(22)]
        counter = collections.Counter(deliciousness)
        meal_occurance = list(counter.items())
        good_meals = 0

        while meal_occurance:
            key, val = meal_occurance.pop()

            for power in powers_of_two:
                if power - key in counter:
                    if key == power - key:
                        good_meals += val * (val - 1) // 2
                    else:
                        good_meals += val * counter[power - key]

            del counter[key]

        return good_meals % 1_000_000_007
