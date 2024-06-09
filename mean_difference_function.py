def md_nre_single_sample(predict, target, n, p):
    return (target ** (1 / n) - predict ** (1 / n)) ** p

print(md_nre_single_sample(99.5, 100, 2, 1))