def solution(s):
    if not s:
        return []

    ns = []

    for i in range(len(s)):
        if i % 2 == 0:
            ns.append(s[i])
        else:
            ns[(i - 1) // 2] += s[i]

    if len(ns[-1]) == 1:
        ns[-1] += '_'

    return ns