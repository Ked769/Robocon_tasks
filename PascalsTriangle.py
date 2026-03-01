class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pasc = [[1]]
        for i in range(1, numRows):
            prev = pasc[-1]
            row = [1]
            for j in range(1, i):
                row.append(prev[j-1] + prev[j])
            row.append(1)
            pasc.append(row)
        return pasc