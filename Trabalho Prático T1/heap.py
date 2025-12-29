class PriorityHeap:
    """
    Fila de prioridade usando heap.
    Menor prioridade numérica = maior prioridade.
    Armazena pares (priority, item).
    Suporte a decrease_key(item, new_key).
    """

    def __init__(self):
        self._a = []  # lista de (key, item)
        self._pos = {}  # item -> indice em _a

    def __len__(self):
        return len(self._a)

    def is_empty(self):
        return not self._a

    def push(self, key, item):
        i = len(self._a)
        self._a.append((key, item))
        self._pos[item] = i
        self._sift_up(i)

    def pop_min(self):
        if not self._a:
            raise IndexError("pop from empty heap")

        root_key, root_item = self._a[0]
        last = self._a.pop()

        del self._pos[root_item]

        if self._a:
            self._a[0] = last
            self._pos[last[1]] = 0
            self._sift_down(0)

        return root_key, root_item

    def decrease_key(self, item, new_key):
        i = self._pos[item]
        old_key, _ = self._a[i]
        if new_key >= old_key:
            return

        self._a[i] = (new_key, item)
        self._sift_up(i)

    def _sift_up(self, i):
        a = self._a
        pos = self._pos
        while i > 0:
            p = (i - 1) // 2
            if a[i][0] < a[p][0]:
                a[i], a[p] = a[p], a[i]
                pos[a[i][1]] = i
                pos[a[p][1]] = p
                i = p
            else:
                break

    def _sift_down(self, i):
        a = self._a
        pos = self._pos
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
                pos[a[i][1]] = i
                pos[a[m][1]] = m
                i = m
            else:
                break
