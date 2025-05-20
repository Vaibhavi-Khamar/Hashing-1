#Time Complexity: O(n), where n is the number of words
#Space Complexity: O(n), to split and store n words

#Using 2 hashmaps. One to map pattern->word. Another to map word->pattern.
#For each character-word pair: If either mapping exists, validate it matches the current pair. If not, create new entries in both maps.
#If any inconsistency is found, return False. If the loop completes without conflict, return True.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split() # break a string into a list of words where words are seperated by spaces

        # Pattern length and number of words must match
        if len(pattern) != len(words):
            return False

        map_p_to_w = {}  # pattern character to word
        map_w_to_p = {}  # word to pattern character

        for i in range(len(pattern)):
            p_char = pattern[i]
            word = words[i]

            # Pattern to word mapping check
            if p_char not in map_p_to_w:
                map_p_to_w[p_char] = word
            elif map_p_to_w[p_char] != word:
                return False

            # Word to pattern mapping check
            if word not in map_w_to_p:
                map_w_to_p[word] = p_char
            elif map_w_to_p[word] != p_char:
                return False

        return True
        

# # Using HashMap and HashSet
# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         words = s.split()

#         # Pattern length must match the number of words
#         if len(pattern) != len(words):
#             return False

#         char_to_word = {}  # Maps pattern character -> word
#         used_words = set()  # Keeps track of words already mapped

#         for i in range(len(pattern)):
#             p_char = pattern[i]
#             word = words[i]

#             if p_char not in char_to_word:
#                 if word in used_words:
#                     return False  # Word already mapped to another character
#                 char_to_word[p_char] = word
#                 used_words.add(word)
#             else:
#                 if char_to_word[p_char] != word:
#                     return False  # Mismatch in established mapping

#         return True