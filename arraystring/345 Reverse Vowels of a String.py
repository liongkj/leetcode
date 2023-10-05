

class Solution:

    def reverseVowelsslow(self, s: str) -> str:
        """
        67ms
        Beats 29.47%of users with Python3

        18.24MB
        Beats 21.71%of users with Python3
        """
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        res = []
        vower_list = [i for i in s if i in vowels]
        for i in range(len(s)):
            if s[i] in vowels:
                res.append(vower_list.pop())
            else:
                res.append(s[i])
        return "".join(res)
    
    """
    46ms
    Beats 92.96%of users with Python3

    17.32MB
    Beats 65.17%of users with Python3
    """

    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        left, right = 0, len(s) - 1
        s = list(s)
        while left < right:
            while left < right and s[left] not in vowels:
                left+=1
            while left < right and s[right] not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
        return "".join(s)

if __name__ == '__main__':
    s = "hello"
    res =(Solution().reverseVowels(s))
    print(res)
    assert res == "holle"