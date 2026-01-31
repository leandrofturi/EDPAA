import math
from typing import List, Tuple, Optional
from BTreeNode import BTreeNode
from diskManager import DiskManager


class BTree:
    def __init__(self, d: int, disk: DiskManager):
        if d < 2:
            raise ValueError("Ordem d deve ser >= 2.")
        self.d = d
        self.disk = disk
        self.max_keys = d - 1
        self.min_keys = math.ceil(d / 2) - 1

        self.root = self.disk.alloc_node(is_leaf=True)

    def search(self, key: int) -> bool:
        return self._search(self.root, key)

    def _search(self, idx: int, key: int) -> bool:
        node = self.disk.read_node(idx)
        i = 0
        while i < node.n_keys and key > node.keys[i]:
            i += 1
        if i < node.n_keys and node.keys[i] == key:
            return True
        if node.is_leaf:
            return False
        return self._search(node.children[i], key)

    def insert(self, key: int, value: int) -> None:
        promoted = self._insert_rec(self.root, key, value)
        if promoted is not None:
            promo_k, promo_v, right_idx = promoted
            old_root = self.root
            new_root = self.disk.alloc_node(is_leaf=False)

            r = self.disk.read_node(new_root)
            r.n_keys = 1
            r.keys[0] = promo_k
            r.values[0] = promo_v
            r.children[0] = old_root
            r.children[1] = right_idx
            self.disk.write_node(new_root, r)
            self.root = new_root

    def _insert_rec(self, idx: int, key: int, value: int) -> Optional[Tuple[int, int, int]]:
        node = self.disk.read_node(idx)

        # update se já existe aqui
        for i in range(node.n_keys):
            if node.keys[i] == key:
                node.values[i] = value
                self.disk.write_node(idx, node)
                return None

        if node.is_leaf:
            keys = node.key_list()
            vals = node.value_list()
            pos = 0
            while pos < len(keys) and keys[pos] < key:
                pos += 1
            keys.insert(pos, key)
            vals.insert(pos, value)

            if len(keys) <= self.max_keys:
                self._write_from_lists(idx, node, keys, vals, node.children)
                return None
            return self._split_overflow(idx, node, keys, vals, node.children)

        # interno: desce
        i = 0
        while i < node.n_keys and key > node.keys[i]:
            i += 1
        child_idx = node.children[i]
        promoted = self._insert_rec(child_idx, key, value)
        if promoted is None:
            return None

        promo_k, promo_v, right_idx = promoted
        keys = node.key_list()
        vals = node.value_list()
        children = node.child_list()

        ins = 0
        while ins < len(keys) and keys[ins] < promo_k:
            ins += 1
        keys.insert(ins, promo_k)
        vals.insert(ins, promo_v)
        children.insert(ins + 1, right_idx)

        if len(keys) <= self.max_keys:
            self._write_from_lists(idx, node, keys, vals, children)
            return None
        return self._split_overflow(idx, node, keys, vals, children)

    def _write_from_lists(self, idx: int, node: BTreeNode, keys: List[int], vals: List[int], children: List[int]) -> None:
        node.n_keys = len(keys)
        for j in range(self.max_keys):
            if j < node.n_keys:
                node.keys[j] = keys[j]
                node.values[j] = vals[j]
            else:
                node.keys[j] = 0
                node.values[j] = 0
        for j in range(self.d):
            node.children[j] = children[j] if j < len(children) else -1
        self.disk.write_node(idx, node)

    def _split_overflow(self, idx: int, node: BTreeNode, keys: List[int], vals: List[int], children: List[int]) -> Tuple[int, int, int]:
        # overflow: len(keys) == d
        mid = len(keys) // 2  # mediana superior para d par
        promo_k = keys[mid]
        promo_v = vals[mid]

        left_keys = keys[:mid]
        left_vals = vals[:mid]
        right_keys = keys[mid + 1:]
        right_vals = vals[mid + 1:]

        is_leaf = bool(node.is_leaf)
        if is_leaf:
            left_children = [-1] * self.d
            right_children = [-1] * self.d
        else:
            left_children = children[: mid + 1]
            right_children = children[mid + 1:]

        # escreve esquerdo no próprio idx
        self._write_from_lists(idx, node, left_keys, left_vals, left_children)

        # cria direito
        right_idx = self.disk.alloc_node(is_leaf=is_leaf)
        rnode = self.disk.read_node(right_idx)
        self._write_from_lists(right_idx, rnode, right_keys, right_vals, right_children)

        return (promo_k, promo_v, right_idx)

    def remove(self, key: int) -> None:
        self._delete(self.root, key)
        # rebalanceio extra em 1 nível: tenta redistribuir 1 chave do irmão direito para o filho esquerdo
        self._rebalance_level(self.root)

        root_node = self.disk.read_node(self.root)
        if root_node.n_keys == 0 and not root_node.is_leaf:
            self.root = root_node.children[0]

    def _delete(self, idx: int, key: int) -> None:
        node = self.disk.read_node(idx)

        i = 0
        while i < node.n_keys and key > node.keys[i]:
            i += 1

        if i < node.n_keys and node.keys[i] == key:
            if node.is_leaf:
                self._delete_from_leaf(idx, node, i)
            else:
                self._delete_from_internal(idx, node, i)
            return

        if node.is_leaf:
            return

        child_pos = i
        child_idx = node.children[child_pos]
        child = self.disk.read_node(child_idx)

        if child.n_keys == self.min_keys:
            child_idx = self._fix_child_underflow(idx, node, child_pos)

        self._delete(child_idx, key)

    def _delete_from_leaf(self, idx: int, node: BTreeNode, pos: int) -> None:
        keys = node.key_list()
        vals = node.value_list()
        keys.pop(pos); vals.pop(pos)
        self._write_from_lists(idx, node, keys, vals, node.children)

    def _delete_from_internal(self, idx: int, node: BTreeNode, pos: int) -> None:
        left_idx = node.children[pos]
        right_idx = node.children[pos + 1]
        left = self.disk.read_node(left_idx)
        right = self.disk.read_node(right_idx)

        if left.n_keys > self.min_keys:
            pk, pv = self._max_in_subtree(left_idx)
            node.keys[pos] = pk; node.values[pos] = pv
            self.disk.write_node(idx, node)
            self._delete(left_idx, pk)
            return

        if right.n_keys > self.min_keys:
            sk, sv = self._min_in_subtree(right_idx)
            node.keys[pos] = sk; node.values[pos] = sv
            self.disk.write_node(idx, node)
            self._delete(right_idx, sk)
            return

        merged_idx = self._merge(idx, node, pos)
        self._delete(merged_idx, key)

    def _min_in_subtree(self, idx: int) -> Tuple[int, int]:
        cur = idx
        while True:
            n = self.disk.read_node(cur)
            if n.is_leaf:
                return (n.keys[0], n.values[0])
            cur = n.children[0]

    def _max_in_subtree(self, idx: int) -> Tuple[int, int]:
        cur = idx
        while True:
            n = self.disk.read_node(cur)
            if n.is_leaf:
                return (n.keys[n.n_keys - 1], n.values[n.n_keys - 1])
            cur = n.children[n.n_keys]

    def _fix_child_underflow(self, parent_idx: int, parent: BTreeNode, child_pos: int) -> int:
        child_idx = parent.children[child_pos]
        child = self.disk.read_node(child_idx)

        if child_pos > 0:
            left_idx = parent.children[child_pos - 1]
            left = self.disk.read_node(left_idx)
            if left.n_keys > self.min_keys:
                self._borrow_from_left(parent_idx, parent, child_pos, left_idx, left, child_idx, child)
                return child_idx

        if child_pos < parent.n_keys:
            right_idx = parent.children[child_pos + 1]
            right = self.disk.read_node(right_idx)
            if right.n_keys > self.min_keys:
                self._borrow_from_right(parent_idx, parent, child_pos, right_idx, right, child_idx, child)
                return child_idx

        if child_pos < parent.n_keys:
            return self._merge(parent_idx, parent, child_pos)
        return self._merge(parent_idx, parent, child_pos - 1)

    def _borrow_from_left(self, parent_idx: int, parent: BTreeNode, child_pos: int,
                          left_idx: int, left: BTreeNode, child_idx: int, child: BTreeNode) -> None:
        ck, cv = child.key_list(), child.value_list()
        lk, lv = left.key_list(), left.value_list()

        ck.insert(0, parent.keys[child_pos - 1])
        cv.insert(0, parent.values[child_pos - 1])

        parent.keys[child_pos - 1] = lk.pop(-1)
        parent.values[child_pos - 1] = lv.pop(-1)

        if not child.is_leaf:
            cch = child.child_list()
            lch = left.child_list()
            cch.insert(0, lch.pop(-1))
            self._write_from_lists(child_idx, child, ck, cv, cch)
            self._write_from_lists(left_idx, left, lk, lv, lch)
        else:
            self._write_from_lists(child_idx, child, ck, cv, child.children)
            self._write_from_lists(left_idx, left, lk, lv, left.children)

        self.disk.write_node(parent_idx, parent)

    def _borrow_from_right(self, parent_idx: int, parent: BTreeNode, child_pos: int,
                           right_idx: int, right: BTreeNode, child_idx: int, child: BTreeNode) -> None:
        ck, cv = child.key_list(), child.value_list()
        rk, rv = right.key_list(), right.value_list()

        ck.append(parent.keys[child_pos])
        cv.append(parent.values[child_pos])

        parent.keys[child_pos] = rk.pop(0)
        parent.values[child_pos] = rv.pop(0)

        if not child.is_leaf:
            cch = child.child_list()
            rch = right.child_list()
            cch.append(rch.pop(0))
            self._write_from_lists(child_idx, child, ck, cv, cch)
            self._write_from_lists(right_idx, right, rk, rv, rch)
        else:
            self._write_from_lists(child_idx, child, ck, cv, child.children)
            self._write_from_lists(right_idx, right, rk, rv, right.children)

        self.disk.write_node(parent_idx, parent)

    def _merge(self, parent_idx: int, parent: BTreeNode, sep_pos: int) -> int:
        left_idx = parent.children[sep_pos]
        right_idx = parent.children[sep_pos + 1]
        left = self.disk.read_node(left_idx)
        right = self.disk.read_node(right_idx)

        lk, lv = left.key_list(), left.value_list()
        rk, rv = right.key_list(), right.value_list()

        lk.append(parent.keys[sep_pos]); lv.append(parent.values[sep_pos])
        lk.extend(rk); lv.extend(rv)

        if not left.is_leaf:
            lch = left.child_list()
            rch = right.child_list()
            lch.extend(rch)
        else:
            lch = left.children

        pk, pv = parent.key_list(), parent.value_list()
        pch = parent.child_list()
        pk.pop(sep_pos); pv.pop(sep_pos); pch.pop(sep_pos + 1)

        self._write_from_lists(left_idx, left, lk, lv, lch)
        self._write_from_lists(parent_idx, parent, pk, pv, pch)
        return left_idx

    def _rebalance_level(self, idx: int) -> None:
        node = self.disk.read_node(idx)
        if node.is_leaf:
            return
        for child_pos in range(node.n_keys):
            left_idx = node.children[child_pos]
            right_idx = node.children[child_pos + 1]
            if left_idx == -1 or right_idx == -1:
                continue
            right = self.disk.read_node(right_idx)
            left = self.disk.read_node(left_idx)
            if right.n_keys > self.min_keys and left.n_keys < self.max_keys:
                self._borrow_from_right(idx, node, child_pos, right_idx, right, left_idx, left)
                node = self.disk.read_node(idx)

    def to_level_order_lines(self) -> List[str]:
        lines: List[str] = []
        q: List[int] = [self.root]
        while q:
            nxt: List[int] = []
            parts: List[str] = []
            for idx in q:
                node = self.disk.read_node(idx)
                s = "["
                for j in range(node.n_keys):
                    s += f"key: {node.keys[j]}, "
                s += "]"
                parts.append(s)
                if not node.is_leaf:
                    for j in range(node.n_keys + 1):
                        c = node.children[j]
                        if c != -1:
                            nxt.append(c)
            lines.append("".join(parts))
            q = nxt
        return lines
