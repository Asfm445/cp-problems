# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def reverse(self,arr):
        return arr[::-1]
    def invert(self,arr):
        for i, val in enumerate(arr):
            if val=="0":
                arr[i]="1"
            else:
                arr[i]="0"
        return arr
    def findKthBit(self, n: int, k: int) -> str:
        prev=["0"]
        for _ in range(n-1):
            prev=prev+["1"]+self.reverse(self.invert(prev))
        return prev[k-1]
        