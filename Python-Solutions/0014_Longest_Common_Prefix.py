'''14.Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 '''


"---------------------------------------------Solution--------------------------------------------"

class Solution(object):
    def longestCommonPrefix(self, strs):
        a = len(min(strs, key=len))
        x = ""
        for i in range(a):
            for word in strs:
                if word[i] != strs[0][i]:
                    return x
            x = x + strs[0][i]
        return x
