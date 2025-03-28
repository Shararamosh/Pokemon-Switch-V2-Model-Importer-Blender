# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Model

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class VertexSize(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = VertexSize()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsVertexSize(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # VertexSize
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # VertexSize
    def Size(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def VertexSizeStart(builder):
    builder.StartObject(1)

def Start(builder):
    VertexSizeStart(builder)

def VertexSizeAddSize(builder, size):
    builder.PrependUint32Slot(0, size, 0)

def AddSize(builder, size):
    VertexSizeAddSize(builder, size)

def VertexSizeEnd(builder):
    return builder.EndObject()

def End(builder):
    return VertexSizeEnd(builder)


class VertexSizeT(object):

    # VertexSizeT
    def __init__(self):
        self.size = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        vertexSize = VertexSize()
        vertexSize.Init(buf, pos)
        return cls.InitFromObj(vertexSize)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, vertexSize):
        x = VertexSizeT()
        x._UnPack(vertexSize)
        return x

    # VertexSizeT
    def _UnPack(self, vertexSize):
        if vertexSize is None:
            return
        self.size = vertexSize.Size()

    # VertexSizeT
    def Pack(self, builder):
        VertexSizeStart(builder)
        VertexSizeAddSize(builder, self.size)
        vertexSize = VertexSizeEnd(builder)
        return vertexSize
