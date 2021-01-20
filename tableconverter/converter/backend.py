from typing import Dict
from io import StringIO
from ..model import Table
from ..util import convert_char_to_html_entity


class AbstractBackend:
    def __init__(self):
        pass

    def convert(self, table: Table) -> str:
        raise NotImplementedError()


class CSVBackend(AbstractBackend):
    def convert(self, table: Table) -> str:
        buf = StringIO()
        if table.header is None:
            h_sz = table.get_max_cols()
            if h_sz > 1:
                buf.write("," * (h_sz - 1))
        else:
            buf.write(",".join(table.header))
        buf.write("\n")
        for row in table.body:
            buf.write(",".join(self.clean_cell(cell) for cell in row))
            buf.write("\n")
        return buf.getvalue()

    @classmethod
    def clean_cell(cls, cell) -> str:
        if cell is None:
            return '""'
        elif type(cell) == str:
            if "," in cell or '"' in cell:
                cell = '"' + cell.replace('"', '""').replace("\n", "\\n") + '"'
            return cell
        else:
            return str(cell)


class MarkdownBackend(AbstractBackend):
    def convert(self, table: Table) -> str:
        buf = StringIO()
        # write header
        if table.header:
            buf.write("|")
            buf.write("|".join(self._clean_cell(c) for c in table.header))
            buf.write("|")
            cols = len(table.header)
        else:
            cols = table.get_max_cols()
            if cols == 0:
                return ""
            buf.write("|" * (cols + 1))
        buf.write("\n|")
        buf.write("|".join("---" for _ in range(cols)))
        buf.write("|\n")
        for row in table.body:
            if not row:
                continue
            buf.write("|")
            buf.write("|".join(self._clean_cell(c) for c in row))
            buf.write("|\n")
        return buf.getvalue()

    @classmethod
    def _clean_cell(cls, cell) -> str:
        if cell is None:
            return ""
        elif type(cell) == str:
            return cls._clean_string(cell)
        else:
            return cls._clean_string(str(cell))

    @classmethod
    def _clean_string(cls, s: str):
        return s.replace("\n", "\\n").replace("\\", "\\\\").replace("|", "\\|")


class HTMLTableBackend(AbstractBackend):
    def convert(self, table: Table) -> str:
        buffer = StringIO()
        buffer.write("<table>\n")
        if table.header is not None:
            buffer.write("  <tr>\n")
            for cell in table.header:
                buffer.write("    <th>")
                if type(cell) != str:
                    cell = str(cell)
                for ch in cell:
                    ch = convert_char_to_html_entity(ch)
                    buffer.write(ch)
                buffer.write("</th>\n")
            buffer.write("  </tr>\n")
        for row in table.body:
            buffer.write("  <tr>\n")
            for cell in row:
                buffer.write("    <td>")
                if type(cell) != str:
                    cell = str(cell)
                for ch in cell:
                    ch = convert_char_to_html_entity(ch)
                    buffer.write(ch)
                buffer.write("</td>\n")
            buffer.write("  </tr>\n")
        buffer.write("</table>")
        return buffer.getvalue()


class JSONArrBackend(AbstractBackend):
    def convert(self, table: Table) -> str:
        import json

        if table.header is None:
            buf = table.body
        else:
            buf = [table.header]
            buf.extend(table.body)
        return json.dumps(buf)


class JSONObjBackend(AbstractBackend):
    def convert(self, table: Table) -> str:
        import json

        if table.header is None:
            raise ValueError("missing table header")
        index_key_map = dict((idx, v) for idx, v in enumerate(table.header))
        buf = []
        for row in table.body:
            data = {}
            for idx, item in enumerate(row):
                key = index_key_map[idx]
                data[key] = item
            buf.append(data)
        return json.dumps(buf)


class BackendFactory:
    _BACKEND_MAP = {
        "html": HTMLTableBackend,
        "md": MarkdownBackend,
        "csv": CSVBackend,
        "json": JSONArrBackend,
        "json-arr": JSONArrBackend,
        "json-obj": JSONObjBackend,
    }  # type: Dict[str, AbstractBackend]

    @classmethod
    def new_instance(cls, fmt):
        if fmt in cls._BACKEND_MAP:
            clz = cls._BACKEND_MAP[fmt]
            return clz()
        raise ValueError("{} backend is not supported".format(fmt))
