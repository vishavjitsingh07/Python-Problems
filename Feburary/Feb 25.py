def baseEquiv(n, m):
    for i in range(2, 33):
        val = int(math.log(n, i)) + 1
        if val == m:
            return "Yes"
    return "No"
