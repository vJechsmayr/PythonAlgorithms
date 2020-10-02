class Solution:
    def mergeOverlappingSpans(self, spans):
        spans = sorted(spans)
        i, j = 0, 1
        while j < len(spans):
            if spans[i][1] < spans[j][0]:   # Non Overlapping
                i += 1
                spans[i] = spans[j]
            else:
                spans[i][1] = max(spans[i][1], spans[j][1])
            j += 1
        return spans[:i+1]

    def partitionLabels(self, S: str) -> List[int]:
        spans = {}
        for i in range (len(S)):
            if S[i] not in spans:
                spans[S[i]] = [i, i]
            else:
                spans[S[i]][1] = i

        # one span [startIndex, endIndex] for each unique character
        # there will be maximum 26 spans
        spans = spans.values()

        nonOverlappingSpans = self.mergeOverlappingSpans(spans)
        return [span[1]-span[0]+1 for span in nonOverlappingSpans]