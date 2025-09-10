# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_que=deque()
        max_que=deque()
        min_que.append(nums[0])
        max_que.append(nums[0])
        a=0
        b=1
        ans=0
        while b<len(nums):
            if max_que[0]-min_que[0]<=limit:
                ans=max(ans,b-a)
                print(a,b)
                while min_que and min_que[-1]>nums[b]:
                    min_que.pop()
                while max_que and max_que[-1]<nums[b]:
                    max_que.pop()
                min_que.append(nums[b])
                max_que.append(nums[b])
                b+=1
            else:
                if min_que[0]==nums[a]:
                    min_que.popleft()
                if max_que[0]==nums[a]:
                    max_que.popleft()
                a+=1
        while min_que and max_que and max_que[0]-min_que[0]>limit:
            if min_que[0]==nums[a]:
                min_que.popleft()
            if max_que[0]==nums[a]:
                max_que.popleft()
            a+=1
        ans=max(b-a,ans)
        return ans

        