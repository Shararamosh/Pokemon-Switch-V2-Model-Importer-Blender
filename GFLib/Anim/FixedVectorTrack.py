# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Anim

import flatbuffers
from flatbuffers.compat import import_numpy

from GFLib.Anim.Vec3 import Vec3T, Vec3

np = import_numpy()

class FixedVectorTrack(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = FixedVectorTrack()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsFixedVectorTrack(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # FixedVectorTrack
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # FixedVectorTrack
    def Co(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            obj = Vec3()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def FixedVectorTrackStart(builder):
    builder.StartObject(1)

def Start(builder):
    FixedVectorTrackStart(builder)

def FixedVectorTrackAddCo(builder, co):
    builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(co), 0)

def AddCo(builder, co):
    FixedVectorTrackAddCo(builder, co)

def FixedVectorTrackEnd(builder):
    return builder.EndObject()

def End(builder):
    return FixedVectorTrackEnd(builder)

try:
    from typing import Optional
except:
    pass

class FixedVectorTrackT(object):

    # FixedVectorTrackT
    def __init__(self):
        self.co = None  # type: Optional[Vec3T]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        fixedVectorTrack = FixedVectorTrack()
        fixedVectorTrack.Init(buf, pos)
        return cls.InitFromObj(fixedVectorTrack)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, fixedVectorTrack):
        x = FixedVectorTrackT()
        x._UnPack(fixedVectorTrack)
        return x

    # FixedVectorTrackT
    def _UnPack(self, fixedVectorTrack):
        if fixedVectorTrack is None:
            return
        if fixedVectorTrack.Co() is not None:
            self.co = Vec3T.InitFromObj(fixedVectorTrack.Co())

    # FixedVectorTrackT
    def Pack(self, builder):
        FixedVectorTrackStart(builder)
        if self.co is not None:
            co = self.co.Pack(builder)
            FixedVectorTrackAddCo(builder, co)
        fixedVectorTrack = FixedVectorTrackEnd(builder)
        return fixedVectorTrack
