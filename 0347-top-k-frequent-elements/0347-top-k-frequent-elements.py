class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqOfNums = {}
        answer = []  

        for num in nums:
            if num in freqOfNums:
                freqOfNums[num] += 1
            else:
                freqOfNums[num] = 1

        heap = []

        for num in freqOfNums:
                heapq.heappush(heap, (-freqOfNums[num], num))

        
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer