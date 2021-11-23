from functools import reduce; fibSequence = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])

print(fibSequence(10))
print(fibSequence(5))
print(fibSequence(6))
