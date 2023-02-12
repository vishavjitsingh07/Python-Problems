class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        d = defaultdict()
        for idx, i in enumerate(board):
            for idx2, j in enumerate(i):
                d[j] = (idx, idx2)

        ans = ""  
        currPosI, currPosJ = (0, 0)
        for idx, i in enumerate(target):
            if d[i] == (currPosI, currPosJ):
                ans+="!"
            else:
                currI, currJ = d[i]
                if currJ - currPosJ < 0:
                    ans += "L"*(currPosJ - currJ)
                if currI - currPosI  < 0:
                    ans += "U"*(currPosI - currI)
                if currJ - currPosJ >= 0:
                    ans += "R"*(currJ - currPosJ)
                if currI - currPosI >= 0:
                    ans += "D"*(currI - currPosI)
                ans+="!"
            (currPosI, currPosJ) = d[i]

        return ans
