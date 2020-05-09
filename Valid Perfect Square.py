class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root_num = math.sqrt(num)
        if root_num.is_integer():
            return True
        else:
            return False
