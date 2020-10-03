from collections import defaultdict, deque


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subgrids = defaultdict(set)
        empty_cells = deque()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    subgrids[(i//3, j//3)].add(board[i][j])
                else:
                    empty_cells.append((i, j))

        def dfs():
            if not empty_cells:
                return True

            row, col = empty_cells[0]
            subgrid = (row//3, col//3)
            for digit in {"1", '2', '3', '4', '5', '6', '7', '8', '9'}:
                if digit not in rows[row] and digit not in cols[col] and digit not in subgrids[subgrid]:
                    board[row][col] = digit
                    rows[row].add(digit)
                    cols[col].add(digit)
                    subgrids[subgrid].add(digit)
                    empty_cells.popleft()
                    if dfs():
                        return True

                    board[row][col] = '.'
                    rows[row].remove(digit)
                    cols[col].remove(digit)
                    subgrids[subgrid].remove(digit)
                    empty_cells.appendleft((row, col))
            return False
        dfs()
        return board
