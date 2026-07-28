# My Solution:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if len(s[i:j]) > max_length and len(s[i:j]) == len(set(s[i:j])):  #Set conversion to check for unique characters
                    max_length = len(s[i:j])
        return max_length


# Time Limit Exceeded above for very large inputs, as it has a time complexity of O(n^3) due to the nested loops and the set conversion.


# Best Solution:

class Solution: 
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


# Explanation for the best solution:
# 1. We use a sliding window approach with two pointers, `left` and `right`, 
# to keep track of the current substring without repeating characters.
# 2. We maintain a set `char_set` to store the characters in the current substring.
# 3. We iterate through the string with the `right` pointer. If the character at `right` is already in the set, we remove characters from the left until we can add the new character.
# 4. We update the maximum length of the substring whenever we add a new character to the set.  
# 5. This approach ensures that we only traverse the string once, resulting in a time complexity of O(n), where n is the length of the string.