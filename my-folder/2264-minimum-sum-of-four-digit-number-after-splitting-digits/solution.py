class Solution:
    def minimumSum(self, num: int) -> int:
        numList = []
        numList.append(num)
        numList = list(map(int, str(numList[0])))
        numList = sorted(numList)
        if numList[0] and numList[1] == 0:
            return numList[2] + numList[3]
        elif numList[0] == 0:
            return (numList[1] * 10) + numList[3] + numList[2]
        else:
            return numList[0]*10 + numList[1] * 10 + numList[2] + numList[3]
