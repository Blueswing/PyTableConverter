from antlr4.InputStream import InputStream
from .frontend import FrontendFactory, AbstractFrontend
from .backend import BackendFactory, AbstractBackend


class Transpiler:
    def __init__(self, frontend: AbstractFrontend, backend: AbstractBackend):
        self._frontend = frontend
        self._backend = backend

    def convert(self, in_stream: InputStream) -> str:
        tbl_obj = self._frontend.get_ir(in_stream)
        return self._backend.convert(tbl_obj)


class TranspilerFactory:
    @classmethod
    def new_transpiler(cls, src_fmt, dst_fmt):
        frontend = FrontendFactory.new_instance(src_fmt)
        backend = BackendFactory.new_instance(dst_fmt)
        return Transpiler(frontend, backend)
