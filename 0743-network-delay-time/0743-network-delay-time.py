class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edges = {i:[] for i in range(n + 1)}

        for u, v, w in times:
            edges[u].append((v, w))
        
        minHeap = [(0, k)]
        t = 0
        visited = set()

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)

            for nei, w2 in edges[n1]:
                if nei not in visited:
                    heapq.heappush(minHeap, (w1 + w2, nei))
        return t if len(visited) == n else -1

