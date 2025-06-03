class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        minOperations = len(blocks)

        for r in range(k - 1, len(blocks)):
            window = blocks[l:r + 1]
            minOperations = min(minOperations, window.count("W"))
            l += 1
        return minOperations


        