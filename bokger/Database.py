from ._dec_io_and_time import OpInfo

class _Database:
    def push(self, opInfo: OpInfo):
        print("push", opInfo)

database = _Database()