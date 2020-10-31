class Solution:
    def neighbours(self, i):
        n = []
        if i >= self.cols:
            n.append(i-self.cols)
        if i + self.cols < self.rows * self.cols:
            n.append(i+self.cols)
        if i % self.cols > 0:
            n.append(i-1)
        if i % self.cols < self.cols - 1:
            n.append(i+1)
        return n        

    def search(self, s):
        if len(self.words) == 0:
            return False
        l = 0
        r = len(self.words) - 1
        while l <= r-1:
            c = (l+r)//2
            if self.words[c] < s:
                l = c+1
            else:
                r = c
        if len(self.words[l]) < len(s):
            return False
        return self.words[l][:len(s)] == s

    def DFS(self, v, s):
        if not self.search(s):
            return
        if s in self.words and s not in self.found:
            self.found.append(s)
        ne = self.neighbours(v)
        for n in ne:
            if self.used[n]:
                continue
            self.used[n] = True
            self.DFS(n, s + self.board[n])
            self.used[n] = False


    def findWords(self, board, words):
        self.found = []
        self.words = sorted(words)
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = [board[i][j] for i in range(len(board)) for j in range(len(board[0]))]
        self.used = [False] * self.cols * self.rows
        for i in range(len(self.board)):
            self.used[i] = True
            self.DFS(i, self.board[i])
            self.used[i] = False
        return self.found

