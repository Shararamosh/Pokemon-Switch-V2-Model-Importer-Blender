# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Model

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Bounds(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Bounds()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBounds(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Bounds
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Bounds
    def Min(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from .Vec3 import Vec3
            obj = Vec3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Bounds
    def Max(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = o + self._tab.Pos
            from .Vec3 import Vec3
            obj = Vec3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def BoundsStart(builder):
    builder.StartObject(2)

def Start(builder):
    BoundsStart(builder)

def BoundsAddMin(builder, min):
    builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(min), 0)

def AddMin(builder, min):
    BoundsAddMin(builder, min)

def BoundsAddMax(builder, max):
    builder.PrependStructSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(max), 0)

def AddMax(builder, max):
    BoundsAddMax(builder, max)

def BoundsEnd(builder):
    return builder.EndObject()

def End(builder):
    return BoundsEnd(builder)
