#!/usr/bin/python3
# Copyright (c) 2016 Bart Massey

words = set()
prefixes = set()
f = open("sowpods.txt", "r")
for w in f:
    w = w.strip()
    if w.isalpha() and w.islower():
        words.add(w)
        for pre in range(1, len(w)):
            prefixes.add(w[0:pre])

n = int(input())
board0 = []
for _ in range(n):
    row = input()
    board0.append([c for c in row.lower()])
counts0 = [int(c) for c in input().split()]

def search(board, counts):
    answers = set()

    def trace(r, c, prefix):
        if board[r][c] == '.':
            return None
        saved = board[r][c]
        p = prefix + saved
        if len(p) > counts[0]:
            return None
        if len(p) == counts[0] and p in words and p not in answers:
            print("found", p)
            answers.add(p)
        if p not in prefixes:
            return None
        board[r][c] = '.'
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue
                if r + dr not in range(n) or c + dc not in range(n):
                    continue
                result = trace(r + dr, c + dc, p)
#               if result != None:
#                   return result
        board[r][c] = saved
        return None

    if counts == []:
        return []
    for r in range(n):
        for c in range(n):
            answer = trace(r, c, "")
            if answer != None:
                return answer
    return None

search(board0, counts0)
