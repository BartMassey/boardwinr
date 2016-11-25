#!/usr/bin/python3
# Copyright (c) 2016 Bart Massey
# This work is made available under the GPL version 3. Please
# see the file `COPYING` in this distribution for license
# information.

# BroadWinr: Solver for WordBrain(TM) puzzles.

import sys

words = set()
prefixes = set()
f = open("words.txt", "r")
for w in f:
    w = w.strip()
    if w.isalpha() and w.islower():
        words.add(w)
        for pre in range(1, len(w)):
            prefixes.add(w[0:pre])

def getRow():
    return list(input().strip().lower())

board0 = [getRow()]
n = len(board0[0])
for _ in range(1, n):
    board0.append(getRow())
counts0 = [int(c) for c in input().split()]

if len(board0) != n:
    print("Row 1 length %d does not match number of rows %d",
          file=sys.stderr)
    exit(1)
for i in range(1, n):
    if len(board0[i]) != n:
        print("Row 1 length %d does not match number of rows %d",
              file=sys.stderr)
        exit(1)

solutions = set()
def search(board, counts, partial):

    def dropTiles(boardish):
        for c in range(n):
            dest = n - 1
            while dest >= 0:
                if boardish[dest][c] != '.':
                    dest -= 1
                    continue
                source = dest
                while source >= 0 and boardish[source][c] == '.':
                    source -= 1
                if source < 0:
                    break
                boardish[dest][c] = boardish[source][c]
                boardish[source][c] = '.'
                dest -= 1
                
    def trace(r, c, prefix):
        if board[r][c] == '.':
            return
        saved = board[r][c]
        p = prefix + saved
        if len(p) > counts[0]:
            return
        if len(p) == counts[0] and p in words:
            newBoard = [r.copy() for r in board]
            newBoard[r][c] = '.'
            dropTiles(newBoard)
            result = search(newBoard, counts[1:], partial + [p])
        if p not in prefixes:
            return
        board[r][c] = '.'
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                if r + dr not in range(n) or c + dc not in range(n):
                    continue
                trace(r + dr, c + dc, p)
        board[r][c] = saved

    if counts == []:
        solutions.add(" ".join(partial))
        return
    for r in range(n):
        for c in range(n):
            answer = trace(r, c, "")

search(board0, counts0, [])
for s in solutions:
    print(s)
