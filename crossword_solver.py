#!/bin/python3

def crosswordPuzzle(crossword, words):
    def solve(crossword_, words_):
        for i in range(len(crossword_)):
            for j in range(len(crossword_[0])):
                if crossword_[i][j] == '-':
                    vertical_candidates = find_vertical_candidates(i, j, crossword_, words_)
                    for c_, c in vertical_candidates:
                        words_.remove(c)
                        start_v = fill_vertical_candidate(i, j, crossword_, c_)
                        horizontal_candidates = find_horizontal_candidates(i, j, crossword_, words_)
                        for d_, d in horizontal_candidates:
                            words_.remove(d)
                            start_h = fill_vertical_candidate(i, j, crossword_, d_)
                            if solve(crossword_, words_):
                                return True

                            words_.append(d)
                            remove_horizontal_candidate(start_h, j, crossword_, d_)

                        if not horizontal_candidates:
                            if solve(crossword_, words_):
                                return True
                        remove_vertical_candidate(start_v, j, crossword_, c)
                        words_.append(c)

                    if not vertical_candidates:
                        horizontal_candidates = find_horizontal_candidates(i, j, crossword_, words_)
                        for d_, d in horizontal_candidates:
                            words_.remove(d)
                            start_h = fill_horizontal_candidate(i, j, crossword_, d_)
                            if solve(crossword_, words_):
                                return True

                            words_.append(d)
                            remove_horizontal_candidate(start_h, j, crossword_, d_)
                    return False
        return True

    transformed_crossword = [list(i) for i in crossword]

    solve(transformed_crossword, str.split(words, ';'))

    return [str.join('', c) for c in transformed_crossword]


def find_vertical_candidates(i, j, puzzle, words):
    start = i
    while puzzle[start][j] != '+' and start >= 0:
        start -= 1

    end = i
    while end < len(puzzle) and puzzle[end][j] != '+':
        end += 1

    s = ''
    for w in range(start + 1, end):
        s += puzzle[w][j]

    word_candidates = get_candidates(s, words)

    return word_candidates


def find_horizontal_candidates(i, j, puzzle, words):
    start = j
    while puzzle[i][start] != '+' and start >= 0:
        start -= 1

    end = j
    while end < len(puzzle) and puzzle[i][end] != '+':
        end += 1

    s = ''
    for w in range(start + 1, end):
        s += puzzle[i][w]

    word_candidates = get_candidates(s, words)

    return word_candidates


def get_candidates(s, words):
    word_candidates = []
    for w in words:
        if len(s) == len(w):
            match = True
            word = ''
            for v in range(len(s)):
                match &= s[v] == w[v] or s[v] == '-'
                if match:
                    if s[v] == w[v]:
                        word += '_'
                    else:
                        word += w[v]

            if match:
                word_candidates.append((word, w))
    return word_candidates


def fill_vertical_candidate(i, j, crossword, c):
    start = i
    while crossword[i][j] != '+' and i >= 0:
        i -= 1

    i += 1
    for c_ in c:
        if c_ != '_':
            crossword[i][j] = c_
        i += 1

    return start


def fill_horizontal_candidate(i, j, crossword, c):
    start = j
    while crossword[i][j] != '+' and j >= 0:
        j -= 1
    j += 1
    for c_ in c:
        if c_ != '_':
            crossword[i][j] = c_
        j += 1

    return start


def remove_vertical_candidate(i, j, crossword, c):
    for c_ in c:
        if c_ != '_':
            crossword[i][j] = '-'
        i += 1


def remove_horizontal_candidate(i, j, crossword, c):
    for c_ in c:
        if c_ != '_':
            crossword[i][j] = '-'
        j += 1


if __name__ == '__main__':
    board = [
        '++++++-+++',
        '++------++',
        '++++++-+++',
        '++++++-+++',
        '+++------+',
        '++++++-+-+',
        '++++++-+-+',
        '++++++++-+',
        '++++++++-+',
        '++++++++-+'
    ]

    w = 'ICELAND;MEXICO;PANAMA;ALMATY'
    ans = crosswordPuzzle(board, w)

    [print(i) for i in ans]
