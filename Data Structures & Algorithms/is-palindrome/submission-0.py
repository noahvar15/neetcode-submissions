class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedText = ''.join(filter(str.isalnum, s.lower()))
        reversedText = ''.join(reversed(cleanedText))
        return cleanedText == reversedText
            