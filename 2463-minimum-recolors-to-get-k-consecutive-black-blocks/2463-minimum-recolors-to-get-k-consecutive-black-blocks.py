class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        answer = len(blocks)

        for i in range(k-1, len(blocks)):
            substring = blocks[l:i + 1]
            answer = min(answer, substring.count("W"))
            l += 1
        return answer

        