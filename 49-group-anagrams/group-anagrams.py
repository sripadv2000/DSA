class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list) # mapping charCount to list of Anagrams

        for word in strs:
            sorted_word = ''.join(sorted(word))
                
            res[sorted_word].append(word)

        return list(res.values())