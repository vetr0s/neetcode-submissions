class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        for idx,ch in enumerate(s):
            sDict[ch] = 1 + sDict.get(ch, 0)
        for idx,ch in enumerate(t):
            tDict[ch] = 1 + tDict.get(ch, 0)
        
        return True if sDict == tDict else False
        