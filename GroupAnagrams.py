# approach-1: using sorting string: O(n * (klogk+k))
# approach-2: using prime number: O(n*k)
# approach-3: using count: O(26n*k)=O(n*k)

#Approach-1:
#Creates a dictionary to store groups of anagrams. Key: the sorted version of the word. Value: list of original strings that match this sorted key.
#Iterates through each string in the input list. Sorts the characters of the string to form a common key for anagrams.
#TC: O(n * (klogk+k)) = O(n*klogk)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        for i in strs:
            sorted_str = "".join(sorted(i))
            if sorted_str not in anagram_map:
                anagram_map[sorted_str] = []
            anagram_map[sorted_str].append(i)
        return list(anagram_map.values())


#Approach-2:
# Groups anagrams by using prime number multiplication.
# Each character is assigned a unique prime, and the product of those primes 
# serves as a unique identifier for a group of anagrams.

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         if not strs:
#             return []

#         # Use a normal dictionary
#         anagram_map = {}

#         for s in strs:
#             # Compute the prime product key for the string
#             key = self.calculate_prime_product(s)

#             # If the key doesn't exist, initialize with an empty list
#             if key not in anagram_map:
#                 anagram_map[key] = []

#             # Append the string to the corresponding anagram group
#             anagram_map[key].append(s)

#         # Return all grouped anagrams
#         return list(anagram_map.values())

#     def calculate_prime_product(self, s: str) -> int:
#         # Prime numbers for each lowercase letter 'a' to 'z'
#         primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
#                   43, 47, 53, 59, 67, 71, 73, 79, 83, 89, 97, 101, 103]

#         product = 1
#         for char in s:
#             product *= primes[ord(char) - ord('a')]

#         return product