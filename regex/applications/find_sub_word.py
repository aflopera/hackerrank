#https://www.hackerrank.com/challenges/find-substring/problem
import re
n = int(input())
texto = ' '.join([input() for _ in range(n)])
i = int(input())
lista = ''
for r in range(i):
    word = input()
    pat = rf'(?<=\w){word}(?=\w)'
    match = re.findall(pat,texto)
    print(len(match))
