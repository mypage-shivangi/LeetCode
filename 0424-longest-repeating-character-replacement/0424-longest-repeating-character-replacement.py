from collections import defaultdict

class Solution:
    def characterReplacement(self, s,k):
        count = defaultdict(int)
        maxf = 0
        left = 0
        maxlen = 0

        for right in range(len(s)):
            count[s[right]] += 1
            maxf = max(maxf, count[s[right]])

            # window size - max frequency character = # of replacements needed
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            maxlen = max(maxlen, right - left + 1)

        return maxlen
