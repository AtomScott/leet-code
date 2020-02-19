#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start

class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        dp = {}
        max_pal = ''
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):

                # Base cases
                if i == j or i+1 == j:
                    is_palindrome = s[i]==s[j]
                # Go deeper in memo
                else:
                    is_palindrome = dp.get((i+1, j-1)) and s[i]==s[j]

                if is_palindrome:
                    max_pal = s[i:j+1] if len(max_pal) < j-i+1 else max_pal
                
                dp[(i,j)] = is_palindrome

        return max_pal

# @lc code=end

