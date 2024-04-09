from typing import List


class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        K = value
        cnt = [0] * K
        for num in nums:
            cnt[num % K] += 1
        ans = 0
        while cnt[ans % K] > 0:
            cnt[ans % K] -= 1
            ans += 1
        return ans
