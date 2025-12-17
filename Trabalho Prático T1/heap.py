class Heap:
    """
    Heap binária para pares (key, item).
    """

    def __init__(self):
        self._a = []  # (key, item)

    def __len__(self):
        return len(self._a)

    def is_empty(self):
        return not self._a

    def push(self, key, item):
        a = self._a
        a.append((key, item))
        self._sift_up(len(a) - 1)

    def pop_min(self):
        a = self._a
        if not a:
            raise IndexError("pop from empty heap")

        root = a[0]
        last = a.pop()
        if a:
            a[0] = last
            self._sift_down(0)
        return root  # (key, item)

    def _sift_up(self, i):
        a = self._a
        while i > 0:
            p = (i - 1) // 2
            if a[i][0] < a[p][0]:
                a[i], a[p] = a[p], a[i]
                i = p
            else:
                break

    def _sift_down(self, i):
        a = self._a
        n = len(a)
        while True:
            l = 2 * i + 1
            r = l + 1
            m = i

            if l < n and a[l][0] < a[m][0]:
                m = l
            if r < n and a[r][0] < a[m][0]:
                m = r

            if m != i:
                a[i], a[m] = a[m], a[i]
                i = m
            else:
                break
