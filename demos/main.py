from antlr4 import FileStream
from tableconverter.converter.transpiler import TranspilerFactory
import os.path


def main():
    in_stream = FileStream(
        os.path.join(os.path.dirname(__file__), "assets", "example.json"), encoding="utf8"
    )
    trans = TranspilerFactory.new_transpiler("json", "md")
    res = trans.convert(in_stream)
    print(res)


if __name__ == "__main__":
    main()
