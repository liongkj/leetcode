"""
149ms
Beats 49.41%of users with Python3

18.50MB
Beats 5.82%of users with Python3
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(list("aeiou"))
        max_count = 0
        s = list(s)
        print(s)
        start = 0
        end = start+k
        count = sum(s[i] in vowels for i in range(start,end))
        max_count = count  # Initialize max_count
        while end < len(s):           

            # print(f"{start=}")
            # print(f"{end=}")
            # print(s[start:end])
            if s[end] in vowels:
                count += 1
            if s[start] in vowels:
                count -= 1 
            # print(count)
            # for i in range(start,end):
            #     if s[i] in vowels:
            #         count+=1
                # print(count)
            max_count = max(count,max_count)

            if max_count == k:
                return k
            end+=1
            start+=1
        return max_count
        

if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    res = Solution().maxVowels(s=s,k=k)
    assert res == 3, "wrong answer"
    print("yay")