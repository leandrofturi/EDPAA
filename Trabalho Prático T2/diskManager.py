import os
import struct
from BTreeNode import BTreeNode


class DiskManager:
    def __init__(self, path: str, d: int):
        self.path = path
        self.d = d
        self.max_keys = d - 1

        self.fmt = (
            "ii" + ("i" * self.max_keys) + ("i" * self.max_keys) + ("i" * d)
        )
        self.node_size = struct.calcsize(self.fmt)

        with open(self.path, "wb"):
            pass
        self._f = open(self.path, "r+b", buffering=0)
        self.next_index = 0

    def alloc_node(self, is_leaf: bool) -> int:
        idx = self.next_index
        self.next_index += 1
        self.write_node(idx, BTreeNode.empty(self.d, is_leaf=is_leaf))
        return idx

    def read_node(self, idx: int) -> BTreeNode:
        self._f.seek(idx * self.node_size)
        data = self._f.read(self.node_size)
        if len(data) != self.node_size:
            raise IOError(f"Falha ao ler nó {idx}.")
        unpacked = struct.unpack(self.fmt, data)

        n_keys = unpacked[0]
        is_leaf = unpacked[1]
        off = 2
        keys = list(unpacked[off: off + self.max_keys])
        off += self.max_keys
        vals = list(unpacked[off: off + self.max_keys])
        off += self.max_keys
        children = list(unpacked[off: off + self.d])

        return BTreeNode(self.d, n_keys, is_leaf, keys, vals, children)

    def write_node(self, idx: int, node: BTreeNode) -> None:
        packed = struct.pack(
            self.fmt, node.n_keys, node.is_leaf, *node.keys, *node.values,
            *node.children
        )
        self._f.seek(idx * self.node_size)
        self._f.write(packed)

    def close_and_delete(self) -> None:
        try:
            self._f.close()
        finally:
            try:
                os.remove(self.path)
            except FileNotFoundError:
                pass
