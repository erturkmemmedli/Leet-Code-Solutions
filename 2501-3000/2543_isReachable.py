class Solution:
    @lru_cache
    def isReachable(self, targetX: int, targetY: int) -> bool:
        return (
            True if targetX == 1 and targetY == 1 else
            self.isReachable(targetX // 2, targetY) if targetX % 2 == 0 else
            self.isReachable(targetX, targetY // 2) if targetY % 2 == 0 else
            self.isReachable(targetX - targetY, targetY) if targetX > targetY else
            self.isReachable(targetX, targetY - targetX) if targetX < targetY else False
        )
