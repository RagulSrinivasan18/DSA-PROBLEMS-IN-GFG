class Solution:
    def longestSubarray(self, arr, k):
        prefix = {0: -1}
        total = 0
        maxi = 0

        for i in range(len(arr)):
            total += arr[i]

            if total - k in prefix:
                length = i - prefix[total - k]
                maxi = max(maxi, length)

            if total not in prefix:
                prefix[total] = i

        return maxi