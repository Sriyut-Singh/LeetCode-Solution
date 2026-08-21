'''
9. Palindrome Number
Hint:-
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''

"-------------------------------------------------------Solution--------------------------------------------------------"
class Solution():
    def isPalindrome(self, x):
        num = str(x)
        rev_num = num[::-1]
        for i in range(0, (len(num) + 1) // 2):
            if num[i] != rev_num[i]:
                return False
        return True

#Test
'''solution = Solution()
x = 121
result = solution.isPalindrome(x)
print(result)'''
