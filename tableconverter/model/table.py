import json
from typing import Optional, List


class Table:
    def __init__(self, header: Optional[List[str]] = None):
        self.header = header
        self.body = []

    def add_row(self, row: List[str]):
        self.body.append(row)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return json.dumps({"header": self.header, "body": self.body})

    def get_max_cols(self):
        mx = 0
        for r in self.body:
            sz = len(r)
            if sz > mx:
                mx = sz
        if self.header is not None:
            sz = len(self.header)
            if sz > mx:
                mx = sz
        return mx
