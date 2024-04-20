for n in range(1, 100):
    m = 1
    cnt = 0
    for i in range(0, n):
        if n < m:
            break
        m += i
        cnt += 1

    print(n, cnt)
