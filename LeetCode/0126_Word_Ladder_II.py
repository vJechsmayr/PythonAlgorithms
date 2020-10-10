class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        from collections import defaultdict
        
        wordList = set(wordList)
        list1 = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = defaultdict(list)
            for a in layer:
                if a == endWord: 
                    list1.extend(b for b in layer[a])
                else:
                    for i in range(len(a)):
                        for j in 'abcdefghijklmnopqrstuvwxyz':
                            new1 = a[:i]+j+a[i+1:]
                            if new1 in wordList:
                                newlayer[new1]+=[k+[new1] for k in layer[a]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return list1