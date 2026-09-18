class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ret = []
        di = defaultdict(list) # sorted key -> []

        for word in strs:
            sorted_word = "".join(sorted(word))
            di[sorted_word].append(word)

        return list(di.values())