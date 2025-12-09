class MM:
    def __init__(self):
        self.min = None
        self.max = None

def minMax(s, n):
    resp = MM()
    if n == 2:
        if s[0] > s[1]:
            resp.min = s[1]
            resp.max = s[0]
        else:
            resp.min = s[0]
            resp.max = s[1]
    else:
        resp = minMax(s, n - 1)
        if s[n - 1] > resp.max:
            resp.max = s[n - 1]
        if s[n - 1] < resp.min:
            resp.min = s[n - 1]
    
    return resp
