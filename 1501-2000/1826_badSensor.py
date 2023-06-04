class Solution:
    def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        i = 0

        while i < len(sensor1):
            if sensor1[i] == sensor2[i]:
                i += 1
            else:
                break

        if i >= len(sensor1) - 1:
            return -1

        first = sensor2[i + 1:] == sensor1[i:len(sensor2) - 1]
        second = sensor1[i + 1:] == sensor2[i:len(sensor2) - 1]

        return -1 if first and second else 1 if first else 2
