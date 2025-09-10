# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.end = []

    def consec(self, num: int) -> bool:
        if not self.end :
            self.end.append([num, 1])
        elif self.end[-1][0] != num:
            self.end.append([num, 1])
        else:
            self.end[-1][1] += 1
        if self.end[-1][0]==self.value and self.end[-1][1]>=self.k:
            return True
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)