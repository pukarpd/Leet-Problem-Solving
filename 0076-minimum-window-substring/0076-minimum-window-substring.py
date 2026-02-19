class Solution:
    def minWindow(self, s, t):
        counter_1 = Counter(t)

        l, r = 0, len(t)
        counter_2 = Counter(s[l:r])
        res = ''

        while r <= len(s):
            # Check if window satisfies counts
            condition = counter_1 <= counter_2

            if not condition:
                if r == len(s):
                    break
                counter_2[s[r]] += 1
                r += 1

            while condition:
                # update result
                if res == '' or len(res) > len(s[l:r]):
                    res = s[l:r]

                counter_2[s[l]] -= 1
                l += 1
                condition = counter_1 <= counter_2

        return res


             


