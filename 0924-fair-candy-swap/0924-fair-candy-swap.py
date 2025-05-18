class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)

        diff = (sumA - sumB) // 2 

        setB = set(bobSizes) 

        for a in aliceSizes:
            b = a - diff
            if b in setB:
                return [a, b]
        