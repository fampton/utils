def lfsr(seed, taps):
    import time
    import sys
    sr, xor = seed, 0
    while 1:
        for t in taps:
            xor += int(sr[t-1])
        if xor%2 == 0.0:
            xor = 0
        else:
            xor = 1
        time.sleep(0.05)
        sr, xor = str(xor) + sr[:-1], 0
        sys.stdout.write('{}\r'.format(sr))
        sys.stdout.flush()
        time.sleep(0.05)

lfsr('1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', (8,7,6,1))
