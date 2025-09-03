class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scr = [-s for s in score] 
        heapq.heapify(scr)
        count = 1
        
        while scr:
            top = abs(heapq.heappop(scr))

            if count == 1:
                score[score.index(top)] = "Gold Medal"
            elif count == 2:
                score[score.index(top)] = "Silver Medal"
            elif count == 3:
                score[score.index(top)] = "Bronze Medal"
            else:
                score[score.index(top)] =  str(count)
            count += 1
        
        return score


      