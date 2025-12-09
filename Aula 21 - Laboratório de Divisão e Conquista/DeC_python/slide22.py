class MM:
    def __init__(self):
        self.min = None
        self.max = None

def minMax(s, ini, fim):
    resp = MM()
    resp2 = MM()
    if ini == fim:
        resp.min = s[ini]
        resp.max = s[ini]
    else:
        meio = (ini + fim) // 2
        resp = minMax(s, ini, meio)
        resp2 = minMax(s, meio + 1, fim)
        if resp.min > resp2.min:
            resp.min = resp2.min
        if resp.max < resp2.max:
            resp.max = resp2.max

    return resp
