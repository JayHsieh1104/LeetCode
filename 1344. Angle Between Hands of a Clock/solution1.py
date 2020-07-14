class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_angle = minutes * 6
        hour_angle = (hour % 12) * 30 + minutes * 0.5
        
        return min(abs(hour_angle - minutes_angle), 360 - abs(hour_angle - minutes_angle))