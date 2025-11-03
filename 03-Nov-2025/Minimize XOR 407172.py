# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:

        num2_bit=0
        # n1=num1
        # n2=num2
        i=0
        while num2>=1<<i:
            if num2&1<<i:
                num2_bit+=1
            i+=1
        ans=0
        i=31
        while num2_bit>0 and i>=0:
            # print(i)
            if num1&1<<i:
                ans|=1<<i
                num2_bit-=1
            # print(ans,i,num2_bit)
            i-=1
        i=0
        while num2_bit>0:
            if num1&1<<i==0:
                ans|=1<<i
                num2_bit-=1
            i+=1
            # print(ans,i,num2_bit)
        return ans

    
        print(num2_bit)


        