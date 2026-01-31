from dataclasses import dataclass
from typing import List


@dataclass
class BTreeNode:
    d: int
    n_keys: int
    is_leaf: int
    keys: List[int]
    values: List[int]
    children: List[int]

    @classmethod
    def empty(cls, d: int, is_leaf: bool) -> "BTreeNode":
        max_keys = d - 1
        return cls(
            d=d,
            n_keys=0,
            is_leaf=1 if is_leaf else 0,
            keys=[0] * max_keys,
            values=[0] * max_keys,
            children=[-1] * d,
        )

    def key_list(self) -> List[int]:
        return self.keys[: self.n_keys]

    def value_list(self) -> List[int]:
        return self.values[: self.n_keys]

    def child_list(self) -> List[int]:
        return self.children[: self.n_keys + 1]
