class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ret = []
        di = defaultdict(list) # sorted key -> []

        for word in strs:
            counts = [0] * 26
            for ch in word:
                counts[ord(ch) - ord("a")] += 1
            di[tuple(counts)].append(word)

        return list(di.values())