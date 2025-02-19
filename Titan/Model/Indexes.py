# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Model

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Indexes(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Indexes()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsIndexes(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Indexes
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Indexes
    def Buffer(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Indexes
    def BufferAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Indexes
    def BufferLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Indexes
    def BufferIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def IndexesStart(builder):
    builder.StartObject(1)

def Start(builder):
    IndexesStart(builder)

def IndexesAddBuffer(builder, buffer):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(buffer), 0)

def AddBuffer(builder, buffer):
    IndexesAddBuffer(builder, buffer)

def IndexesStartBufferVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartBufferVector(builder, numElems):
    return IndexesStartBufferVector(builder, numElems)

def IndexesEnd(builder):
    return builder.EndObject()

def End(builder):
    return IndexesEnd(builder)

try:
    from typing import List
except:
    pass

class IndexesT(object):

    # IndexesT
    def __init__(self):
        self.buffer = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        indexes = Indexes()
        indexes.Init(buf, pos)
        return cls.InitFromObj(indexes)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, indexes):
        x = IndexesT()
        x._UnPack(indexes)
        return x

    # IndexesT
    def _UnPack(self, indexes):
        if indexes is None:
            return
        if not indexes.BufferIsNone():
            if np is None:
                self.buffer = []
                for i in range(indexes.BufferLength()):
                    self.buffer.append(indexes.Buffer(i))
            else:
                self.buffer = indexes.BufferAsNumpy()

    # IndexesT
    def Pack(self, builder):
        if self.buffer is not None:
            if np is not None and type(self.buffer) is np.ndarray:
                buffer = builder.CreateNumpyVector(self.buffer)
            else:
                IndexesStartBufferVector(builder, len(self.buffer))
                for i in reversed(range(len(self.buffer))):
                    builder.PrependUint8(self.buffer[i])
                buffer = builder.EndVector()
        IndexesStart(builder)
        if self.buffer is not None:
            IndexesAddBuffer(builder, buffer)
        indexes = IndexesEnd(builder)
        return indexes
