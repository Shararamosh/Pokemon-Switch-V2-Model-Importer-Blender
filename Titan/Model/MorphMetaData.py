# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Model

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MorphMetaData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MorphMetaData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMorphMetaData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MorphMetaData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MorphMetaData
    def MorphIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MorphMetaData
    def MorphName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MorphMetaData
    def MorphType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

def MorphMetaDataStart(builder):
    builder.StartObject(3)

def Start(builder):
    MorphMetaDataStart(builder)

def MorphMetaDataAddMorphIndex(builder, morphIndex):
    builder.PrependUint32Slot(0, morphIndex, 0)

def AddMorphIndex(builder, morphIndex):
    MorphMetaDataAddMorphIndex(builder, morphIndex)

def MorphMetaDataAddMorphName(builder, morphName):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(morphName), 0)

def AddMorphName(builder, morphName):
    MorphMetaDataAddMorphName(builder, morphName)

def MorphMetaDataAddMorphType(builder, morphType):
    builder.PrependUint8Slot(2, morphType, 0)

def AddMorphType(builder, morphType):
    MorphMetaDataAddMorphType(builder, morphType)

def MorphMetaDataEnd(builder):
    return builder.EndObject()

def End(builder):
    return MorphMetaDataEnd(builder)


class MorphMetaDataT(object):

    # MorphMetaDataT
    def __init__(self):
        self.morphIndex = 0  # type: int
        self.morphName = None  # type: str
        self.morphType = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        morphMetaData = MorphMetaData()
        morphMetaData.Init(buf, pos)
        return cls.InitFromObj(morphMetaData)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, morphMetaData):
        x = MorphMetaDataT()
        x._UnPack(morphMetaData)
        return x

    # MorphMetaDataT
    def _UnPack(self, morphMetaData):
        if morphMetaData is None:
            return
        self.morphIndex = morphMetaData.MorphIndex()
        self.morphName = morphMetaData.MorphName()
        self.morphType = morphMetaData.MorphType()

    # MorphMetaDataT
    def Pack(self, builder):
        if self.morphName is not None:
            morphName = builder.CreateString(self.morphName)
        MorphMetaDataStart(builder)
        MorphMetaDataAddMorphIndex(builder, self.morphIndex)
        if self.morphName is not None:
            MorphMetaDataAddMorphName(builder, morphName)
        MorphMetaDataAddMorphType(builder, self.morphType)
        morphMetaData = MorphMetaDataEnd(builder)
        return morphMetaData
