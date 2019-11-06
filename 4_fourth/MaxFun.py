def maxfun(s, *args):
    sums = []
    for func in args:
        currentSum = 0
        for i in s:
            currentSum += func(i)
        sums.append(currentSum)
    maxSum = sums[0]
    f = 0
    for i in range(0, args.__len__()):
        if maxSum < sums[i]:
            maxSum = sums[i]
            f = i
        elif maxSum == sums[i]:
            f = i
    return args[f]
