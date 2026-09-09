'''
4032. Longest Subarray With at Most K Distinct Prime Factors

You are given an integer array nums consisting of positive integers and an integer k.
The prime factor set of a subarray is the union of the distinct prime factors of all its elements.
Return the length of the longest subarray whose prime factor set contains at most k distinct prime factors. If no such subarray exists, return 0.

Example 1:
Input: nums = [7,6,10,12,11], k = 3
Output: 3

Explanation:
Consider the subarray [6, 10, 12]:
The distinct prime factors of 6 are {2, 3}.
The distinct prime factors of 10 are {2, 5}.
The distinct prime factors of 12 are {2, 3}.
The union of these sets is {2, 3, 5}, which contains 3 distinct prime factors.
No longer subarray satisfies the condition. Therefore, the answer is 3.

Example 2:
Input: nums = [4,6,9,18], k = 4
Output: 4

Explanation:
Consider the entire array [4, 6, 9, 18]:
The distinct prime factors of 4 are {2}.
The distinct prime factors of 6 are {2, 3}.
The distinct prime factors of 9 are {3}.
The distinct prime factors of 18 are {2, 3}.
The union of these sets is {2, 3}, which contains 2 distinct prime factors.
Since 2 <= 4, the entire array is valid. Therefore, the answer is 4.

Example 3:
Input: nums = [6,10,15], k = 2
Output: 1

Explanation:
Every subarray of length at least 2 has prime factor set {2, 3, 5}, which contains 3 distinct prime factors.
Since 3 > 2, only subarrays of length 1 are valid. Therefore, the answer is 1.

Constraints:
1 <= nums.length <= 105
2 <= nums[i] <= 105
1 <= k <= 104

'''

"-----------------------------------------------------------------Solution-----------------------------------------------------------------"

class Solution:
    def longestSubarray(self, nums, k):
        max_num = max(nums)

        # Smallest Prime Factor
        spf = list(range(max_num + 1))

        for i in range(2, int(max_num ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, max_num + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def get_factors(x):
            factors = set()

            while x > 1:
                p = spf[x]
                factors.add(p)

                while x % p == 0:
                    x //= p

            return factors

        # Prime factors of every number
        factors = [get_factors(x) for x in nums]

        count = {}
        distinct = 0
        left = 0
        ans = 0

        for right in range(len(nums)):
            for p in factors[right]:
                if p not in count:
                    count[p] = 0
                if count[p] == 0:
                    distinct += 1
                count[p] += 1

            while distinct > k:
                for p in factors[left]:
                    count[p] -= 1
                    if count[p] == 0:
                        distinct -= 1
                left += 1

            ans = max(ans, right - left + 1)

        return ans
