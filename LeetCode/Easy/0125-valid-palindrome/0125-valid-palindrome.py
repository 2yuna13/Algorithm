class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = [i for i in s.lower() if i.isalnum()]
        
        print(s_list)
        
        if s_list == s_list[::-1]:
            return True
        else:
            False