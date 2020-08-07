class SudokuSolver:
    def __init__(self, printer, board) -> None:
        from collections import defaultdict
        self.printer = printer
        self.board = board
        self.stats = defaultdict(int)
        # minimum stack required
        # import sys
        # sys.setrecursionlimit(57)

    def solve(self, stop_at_first_solution=True) -> bool:

        def helper(board):
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == '.':
                        candidates = self.find_candidates(row, col)

                        for c in candidates:
                            board[row][col] = c
                            self.stats['attempts'] += 1

                            self.printer.print(board, stats=self.stats)

                            self.stats['stack_in_use'] += 1
                            self.stats['max_stack_used'] = \
                                max(self.stats['max_stack_used'], self.stats['stack_in_use'])

                            r = helper(board)

                            self.stats['stack_in_use'] -= 1
                            if r:
                                if stop_at_first_solution:
                                    return True
                                self.stats['solutions'] += 1

                            board[row][col] = '.'
                            self.printer.print(board, stats=self.stats)

                        return False
            return True

        r = helper(self.board)
        self.printer.print(self.board, stats=self.stats)
        return r

    def find_candidates(self, row, col):
        board = self.board
        potential = list(map(str, list(range(1, 10))))
        candidates = [i for i in potential]

        col_vals = []
        for i in range(len(board[0])):
            if board[row][i].isdigit():
                col_vals.append(board[row][i])

        row_vals = []
        for i in range(len(board)):
            if board[i][col].isdigit():
                row_vals.append(board[i][col])

        square_vals = []
        r, c = row // 3 * 3, col // 3 * 3
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if board[i][j].isdigit():
                    square_vals.append(board[i][j])

        for p in potential:
            if p in col_vals:
                candidates.remove(p)
            elif p in row_vals:
                candidates.remove(p)
            elif p in square_vals:
                candidates.remove(p)

        return candidates


class Printer:
    def print(self, b, stats=None):
        pass


import matplotlib.pyplot as plt


class MatPlotLibPrinter(Printer):

    def __init__(self, initial_state) -> None:
        b_ = [[float(j) if j.isdigit() else 0 for j in i] for i in initial_state]

        plt.subplots(figsize=(5, 6))
        self.h = plt.imshow(b_, cmap="hot_r")
        self.t = plt.text(x=0.01, y=0.01, s='', transform=plt.gcf().transFigure)
        plt.colorbar()
        plt.axis(False)

    def print(self, b, stats=None):
        text = []
        if stats:
            for k in stats.keys():
                v = stats[k]
                text.append('{0}={1}'.format(k, v))

        b_ = [[float(j) if j.isdigit() else 0 for j in i] for i in b]

        self.h.set_data(b_)
        self.t.set_text('\n'.join(text))
        plt.pause(10 ** -4)
        # plt.pause(0.1)
        plt.draw()


class StdoutPrinter(Printer):
    def print(self, b, stats=None):
        for i in b:
            print(i)
        print(str.join('', ['-' for _ in range(50)]))


if __name__ == '__main__':
    board_to_solve = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    printer_matplotlib = MatPlotLibPrinter(board_to_solve)
    printer_stdout = StdoutPrinter()

    b = SudokuSolver(printer_matplotlib, board_to_solve).solve(stop_at_first_solution=True)
    print(b)
    plt.show()
