class Solution:
    def countPoints(self, rings: str) -> int:
        answer = 0
        placements = defaultdict(lambda: "")

        for i in range(1, len(rings), +2):
            placements[rings[i]] += rings[i - 1]

        for p in placements:
            if ("B" in placements[p] and "G" in placements[p] and "R" in placements[p]):
                answer += 1
        
        return answer