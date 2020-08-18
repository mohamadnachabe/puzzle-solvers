class Solution:
    def __init__(self):
        self.memo = {}

    def minDistance(self, word1: str, word2: str):

        if (word1, word2) in self.memo:
            return self.memo[(word1, word2)]

        if word1 == word2:
            self.memo[(word1, word2)] = 0
        if len(word1) == 0 or len(word2) == 0:
            self.memo[(word1, word2)] = abs(len(word1) - len(word2))
        elif word1[0] == word2[0]:
            self.memo[(word1, word2)] = self.minDistance(word1[1:], word2[1:])
        else:
            self.memo[(word1, word2)] = 1 + min(
                min(self.minDistance(word1[1:], word2), self.minDistance(word1[1:], word2[1:])),
                self.minDistance(word1, word2[1:]))

        return self.memo[(word1, word2)]


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance("dinitrophenylhydrazine", "acetylphenylhydrazine"))
