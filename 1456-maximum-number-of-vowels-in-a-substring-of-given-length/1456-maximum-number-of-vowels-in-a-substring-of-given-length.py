class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        count = sum(1 for ch in s[:k] if ch in vowels)
        print(count)
        max_count = count

        for i in range(k, len(s)): 
            if s[i] in vowels: 
                count += 1 
            if s[i-k] in vowels: 
                count -= 1 
            max_count = max(max_count, count)

        return max_count


        # O ( n * k windows as you have to calculate the vowel count for each window)
        # i, j, res = 0, k-1, float('-inf')

        # while j < len(s): 
        #     newstring = s[i:j+1]
        #     temp = 0 
        #     for k in range(len(newstring)): 
        #         if newstring[k] in vowels: 
        #             temp += 1 
        #     res = max(res, temp)
        #     i += 1
        #     j += 1 
        # return res 
