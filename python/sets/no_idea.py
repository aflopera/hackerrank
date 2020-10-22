n,m = [int(i) for i in input().split()]
eles = [int(i) for i in input().split()]
a = set([int(i) for i in input().split()])
b = set([int(i) for i in input().split()])
vals = [1 if i in a else -1 if i in b else 0 for i in eles]
print(sum(vals))
