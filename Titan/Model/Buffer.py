# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Model

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Buffer(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Buffer()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBuffer(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Buffer
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Buffer
    def IndexBuffer(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Titan.Model.Indexes import Indexes
            obj = Indexes()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Buffer
    def IndexBufferLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Buffer
    def IndexBufferIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # Buffer
    def VertexBuffer(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Titan.Model.Vertices import Vertices
            obj = Vertices()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Buffer
    def VertexBufferLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Buffer
    def VertexBufferIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Buffer
    def Morphs(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Titan.Model.Morphs import Morphs
            obj = Morphs()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Buffer
    def MorphsLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Buffer
    def MorphsIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def BufferStart(builder):
    builder.StartObject(3)

def Start(builder):
    BufferStart(builder)

def BufferAddIndexBuffer(builder, indexBuffer):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(indexBuffer), 0)

def AddIndexBuffer(builder, indexBuffer):
    BufferAddIndexBuffer(builder, indexBuffer)

def BufferStartIndexBufferVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartIndexBufferVector(builder, numElems):
    return BufferStartIndexBufferVector(builder, numElems)

def BufferAddVertexBuffer(builder, vertexBuffer):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(vertexBuffer), 0)

def AddVertexBuffer(builder, vertexBuffer):
    BufferAddVertexBuffer(builder, vertexBuffer)

def BufferStartVertexBufferVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartVertexBufferVector(builder, numElems):
    return BufferStartVertexBufferVector(builder, numElems)

def BufferAddMorphs(builder, morphs):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(morphs), 0)

def AddMorphs(builder, morphs):
    BufferAddMorphs(builder, morphs)

def BufferStartMorphsVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartMorphsVector(builder, numElems):
    return BufferStartMorphsVector(builder, numElems)

def BufferEnd(builder):
    return builder.EndObject()

def End(builder):
    return BufferEnd(builder)

import Titan.Model.Indexes
import Titan.Model.Morphs
import Titan.Model.Vertices
try:
    from typing import List
except:
    pass

class BufferT(object):

    # BufferT
    def __init__(self):
        self.indexBuffer = None  # type: List[Titan.Model.Indexes.IndexesT]
        self.vertexBuffer = None  # type: List[Titan.Model.Vertices.VerticesT]
        self.morphs = None  # type: List[Titan.Model.Morphs.MorphsT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        buffer = Buffer()
        buffer.Init(buf, pos)
        return cls.InitFromObj(buffer)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, buffer):
        x = BufferT()
        x._UnPack(buffer)
        return x

    # BufferT
    def _UnPack(self, buffer):
        if buffer is None:
            return
        if not buffer.IndexBufferIsNone():
            self.indexBuffer = []
            for i in range(buffer.IndexBufferLength()):
                if buffer.IndexBuffer(i) is None:
                    self.indexBuffer.append(None)
                else:
                    indexes_ = Titan.Model.Indexes.IndexesT.InitFromObj(buffer.IndexBuffer(i))
                    self.indexBuffer.append(indexes_)
        if not buffer.VertexBufferIsNone():
            self.vertexBuffer = []
            for i in range(buffer.VertexBufferLength()):
                if buffer.VertexBuffer(i) is None:
                    self.vertexBuffer.append(None)
                else:
                    vertices_ = Titan.Model.Vertices.VerticesT.InitFromObj(buffer.VertexBuffer(i))
                    self.vertexBuffer.append(vertices_)
        if not buffer.MorphsIsNone():
            self.morphs = []
            for i in range(buffer.MorphsLength()):
                if buffer.Morphs(i) is None:
                    self.morphs.append(None)
                else:
                    morphs_ = Titan.Model.Morphs.MorphsT.InitFromObj(buffer.Morphs(i))
                    self.morphs.append(morphs_)

    # BufferT
    def Pack(self, builder):
        if self.indexBuffer is not None:
            indexBufferlist = []
            for i in range(len(self.indexBuffer)):
                indexBufferlist.append(self.indexBuffer[i].Pack(builder))
            BufferStartIndexBufferVector(builder, len(self.indexBuffer))
            for i in reversed(range(len(self.indexBuffer))):
                builder.PrependUOffsetTRelative(indexBufferlist[i])
            indexBuffer = builder.EndVector()
        if self.vertexBuffer is not None:
            vertexBufferlist = []
            for i in range(len(self.vertexBuffer)):
                vertexBufferlist.append(self.vertexBuffer[i].Pack(builder))
            BufferStartVertexBufferVector(builder, len(self.vertexBuffer))
            for i in reversed(range(len(self.vertexBuffer))):
                builder.PrependUOffsetTRelative(vertexBufferlist[i])
            vertexBuffer = builder.EndVector()
        if self.morphs is not None:
            morphslist = []
            for i in range(len(self.morphs)):
                morphslist.append(self.morphs[i].Pack(builder))
            BufferStartMorphsVector(builder, len(self.morphs))
            for i in reversed(range(len(self.morphs))):
                builder.PrependUOffsetTRelative(morphslist[i])
            morphs = builder.EndVector()
        BufferStart(builder)
        if self.indexBuffer is not None:
            BufferAddIndexBuffer(builder, indexBuffer)
        if self.vertexBuffer is not None:
            BufferAddVertexBuffer(builder, vertexBuffer)
        if self.morphs is not None:
            BufferAddMorphs(builder, morphs)
        buffer = BufferEnd(builder)
        return buffer
