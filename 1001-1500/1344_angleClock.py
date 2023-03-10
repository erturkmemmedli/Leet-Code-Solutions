class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_big_portion = hour // 3
        hour_small_portion = hour % 3
        hour_hand = (hour_big_portion * 15 + hour_small_portion * 5) % 60
        minute_effect_on_hour = minutes / 12
        hour_hand += minute_effect_on_hour
        angle = abs(hour_hand - minutes) * 6
        if angle > 180:
            angle = 360 - angle
        return angle
