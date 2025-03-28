# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Model

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Vec4(object):
    __slots__ = ['_tab']

    @classmethod
    def SizeOf(cls):
        return 16

    # Vec4
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Vec4
    def W(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # Vec4
    def X(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # Vec4
    def Y(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))
    # Vec4
    def Z(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(12))

def CreateVec4(builder, w, x, y, z):
    builder.Prep(4, 16)
    builder.PrependFloat32(z)
    builder.PrependFloat32(y)
    builder.PrependFloat32(x)
    builder.PrependFloat32(w)
    return builder.Offset()


class Vec4T(object):

    # Vec4T
    def __init__(self):
        self.w = 0.0  # type: float
        self.x = 0.0  # type: float
        self.y = 0.0  # type: float
        self.z = 0.0  # type: float

    @classmethod
    def InitFromBuf(cls, buf, pos):
        vec4 = Vec4()
        vec4.Init(buf, pos)
        return cls.InitFromObj(vec4)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, vec4):
        x = Vec4T()
        x._UnPack(vec4)
        return x

    # Vec4T
    def _UnPack(self, vec4):
        if vec4 is None:
            return
        self.w = vec4.W()
        self.x = vec4.X()
        self.y = vec4.Y()
        self.z = vec4.Z()

    # Vec4T
    def Pack(self, builder):
        return CreateVec4(builder, self.w, self.x, self.y, self.z)
