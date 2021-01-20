from antlr4.InputStream import InputStream
from tableconverter.converter.frontend import CSVFrontend


def _get_stream(s):
    return InputStream(s)


def test_csv():
    frontend = CSVFrontend()
    table = frontend.get_ir(_get_stream("1,2,3,4,5\n,2,2,"))
    print(table)
