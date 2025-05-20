# Linked List/ List/ Array can be used but search will become O(n). 
# Hence, use HashMap to make search O(logn).
# Another approach: 1 hashmap (for s), 1 hashset (for t) = O(n)

#Time Complexity: O(n), where n is the length of the strings
#Space Complexity: O(1), since the character mappings are limited to 256 ASCII characters

# 2 hashmaps
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If the strings are of different lengths, they cannot be isomorphic
        if len(s) != len(t):
            return False

        mapS = {}  # Maps characters from s -> t
        mapT = {}  # Maps characters from t -> s

        for i in range(len(s)):
            # Check or assign mapping from s to t
            if s[i] not in mapS:
                mapS[s[i]] = t[i]
            else:
                # If already mapped, ensure it maps to the current character in t
                if mapS[s[i]] != t[i]:
                    return False

            # Check or assign mapping from t to s (reverse check)
            if t[i] not in mapT:
                mapT[t[i]] = s[i]
            else:
                # If already mapped, ensure it maps to the current character in s
                if mapT[t[i]] != s[i]:
                    return False

        # If all mappings are consistent, return True
        return True

# # 1 hashmap and 1 hashset
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         char_map = {}      # Maps characters from s to t
#         mapped_set = set() # Tracks characters already mapped to in t

#         for i in range(len(s)):
#             c = s[i]
#             d = t[i]

#             if c not in char_map:
#                 # If d is already mapped by some other character, return False
#                 if d in mapped_set:
#                     return False
#                 # Establish the mapping and record it
#                 char_map[c] = d
#                 mapped_set.add(d)
#             else:
#                 # Existing mapping must match the current character
#                 if char_map[c] != d:
#                     return False

#         return True  