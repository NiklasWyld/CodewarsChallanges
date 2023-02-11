import re

def time_correct(t):
    if not t:
        return t
    
    if not re.match('\d\d:\d\d:\d\d$', t):
        return

    h = int(t.split(':')[0])
    m = int(t.split(':')[1])
    s = int(t.split(':')[2])

    if h >= 24:
        h = h % 24
    if m >= 60:
        m -= 60
        h += 1
    if s >= 60:
        s -= 60
        m += 1
    
    return "{0:0>2}:{1:0>2}:{2:0>2}".format(h, m, s)
