
class Solution:
    def countTriplet(self, arr):
        arr.sort()
        count = 0

        for i in range(2, len(arr)):
            if i > 2 and arr[i] == arr[i-1]:
                continue

            l = 0
            r = i - 1

            while l < r:
                target = arr[l] + arr[r]

                if target == arr[i]:
                    count += 1
                    lef = arr[l]
                    rig = arr[r]

                    while l < r and lef == arr[l]:
                        l += 1

                    while l < r and rig == arr[r]:
                        r -= 1

                elif target < arr[i]:
                    l += 1

                else:
                    r -= 1

        return count
