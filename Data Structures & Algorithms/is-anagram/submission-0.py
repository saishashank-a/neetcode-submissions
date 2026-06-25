class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        else:
            hashmap = {}
            for char in s:
                if char in hashmap:
                    hashmap[char] += 1
                else: 
                    hashmap[char] = 1
            for char in t:
                if char in hashmap and hashmap[char] > 0:
                    hashmap[char] -= 1
                else:
                    return False
            return True