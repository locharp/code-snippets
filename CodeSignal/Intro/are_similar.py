def solution(a, b):
    first = True
    pair = []

    for i in range(len(a)):
        if a[i] != b[i]:
            if first:
                pair = [a[i], b[i]]
                first = False
            else:
                if [b[i], a[i]] == pair:
                    pair = []
                else:
                    return False

    return first or not pair