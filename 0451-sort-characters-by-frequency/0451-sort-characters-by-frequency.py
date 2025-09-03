class Solution:
    def frequencySort(self, s: str) -> str:
        freqOfCharacters = {}

        for c in s:
            if c in freqOfCharacters:
                freqOfCharacters[c] += 1
            else:
                freqOfCharacters[c] = 1
        
        heap = []

        for c in freqOfCharacters:
            heapq.heappush(heap, (-freqOfCharacters[c], c))

        answer = ""
        
        while heap:
            freq, char = heapq.heappop(heap)
            answer += char * -freq
        
        return answer
