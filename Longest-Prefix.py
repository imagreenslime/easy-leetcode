#https://leetcode.com/problems/longest-common-prefix/submissions/
class Solution:
    def longestCommonPrefix(self, strs):
        prefix = min(strs, key=len)
        # prefix is set to the shortest word to save time
        for word in strs:
            # loop thhrough each word once
            for num, words in enumerate(zip(prefix, word)):
                # then we compare the shortest common prefix with each word
                # the use of zip in this instance makes the time complexity 0(n * prefix) instead of O(n*n)
                if words[0] != words[1]:
                    # and if the the letters dont match, we take the new prefix9
                    prefix = prefix[:num]
        return prefix