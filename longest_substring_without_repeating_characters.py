class Solution(object):
    def lengthOfLongestSubstring(self, s):
        s_len = len(s)
        map = {}
        count = 0
        j = 0
        for i in range(s_len):
            try:
                j = max(map[s[i]], j)
            except KeyError:
                pass
            count = max(count, i - j + 1)
            map[s[i]] = i + 1
        return count