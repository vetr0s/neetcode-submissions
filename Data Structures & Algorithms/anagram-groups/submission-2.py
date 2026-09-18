class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=defaultdict()
        for word in strs:
            sorted_word = sorted(word)
            lable = "".join(sorted_word)

            if lable not in map:
                map[lable] = []
            
            map[lable].append(word)
        return list(map.values())