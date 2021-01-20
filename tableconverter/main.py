"""
Console script

Usage:
    tableconverter <args>
"""
import sys
import os
import click
from antlr4 import FileStream, StdinStream
from tableconverter.converter.transpiler import TranspilerFactory


def _extract_file_type(file: str) -> str:
    if not file:
        return ""
    _, ext = os.path.splitext(file)
    return ext.lstrip(".")


@click.command()
@click.argument("file", required=False)
@click.option("-s", "--src", required=False, help="source format")
@click.option("-d", "--dst", required=True, help="destination format")
@click.option("-o", "--output", required=False, help="output file")
def main(file, src, dst, output):
    file_type = _extract_file_type(file)
    if file:
        if not src:
            if file_type:
                src = file_type
            else:
                raise ValueError("unknown source type")
        in_stream = FileStream(file, "utf8")
    else:
        if not src:
            raise ValueError("unknown source type")
        in_stream = StdinStream("utf8")
    trans = TranspilerFactory.new_transpiler(src, dst)
    res = trans.convert(in_stream)
    if output:
        with open(output, "wt") as f:
            print(res, file=f)
    else:
        print(res)


if __name__ == "__main__":
    sys.exit(main())
