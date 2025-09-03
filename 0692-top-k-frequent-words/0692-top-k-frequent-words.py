class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqOfWords = {}
        heap = []
        answer = []

        for word in words:
            if word in freqOfWords:
                freqOfWords[word] += 1
            else:
                freqOfWords[word] = 1
        
        for word in freqOfWords:
            heapq.heappush(heap, (-freqOfWords[word], word))

        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])

        return answer