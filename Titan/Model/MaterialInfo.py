# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Model

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MaterialInfo(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MaterialInfo()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMaterialInfo(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MaterialInfo
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MaterialInfo
    def PolyCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MaterialInfo
    def PolyOffset(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MaterialInfo
    def ShUnk3(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MaterialInfo
    def MaterialName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # MaterialInfo
    def ShUnk4(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return -1

def MaterialInfoStart(builder):
    builder.StartObject(5)

def Start(builder):
    MaterialInfoStart(builder)

def MaterialInfoAddPolyCount(builder, polyCount):
    builder.PrependUint32Slot(0, polyCount, 0)

def AddPolyCount(builder, polyCount):
    MaterialInfoAddPolyCount(builder, polyCount)

def MaterialInfoAddPolyOffset(builder, polyOffset):
    builder.PrependUint32Slot(1, polyOffset, 0)

def AddPolyOffset(builder, polyOffset):
    MaterialInfoAddPolyOffset(builder, polyOffset)

def MaterialInfoAddShUnk3(builder, shUnk3):
    builder.PrependUint32Slot(2, shUnk3, 0)

def AddShUnk3(builder, shUnk3):
    MaterialInfoAddShUnk3(builder, shUnk3)

def MaterialInfoAddMaterialName(builder, materialName):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(materialName), 0)

def AddMaterialName(builder, materialName):
    MaterialInfoAddMaterialName(builder, materialName)

def MaterialInfoAddShUnk4(builder, shUnk4):
    builder.PrependInt32Slot(4, shUnk4, -1)

def AddShUnk4(builder, shUnk4):
    MaterialInfoAddShUnk4(builder, shUnk4)

def MaterialInfoEnd(builder):
    return builder.EndObject()

def End(builder):
    return MaterialInfoEnd(builder)


class MaterialInfoT(object):

    # MaterialInfoT
    def __init__(self):
        self.polyCount = 0  # type: int
        self.polyOffset = 0  # type: int
        self.shUnk3 = 0  # type: int
        self.materialName = None  # type: str
        self.shUnk4 = -1  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        materialInfo = MaterialInfo()
        materialInfo.Init(buf, pos)
        return cls.InitFromObj(materialInfo)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, materialInfo):
        x = MaterialInfoT()
        x._UnPack(materialInfo)
        return x

    # MaterialInfoT
    def _UnPack(self, materialInfo):
        if materialInfo is None:
            return
        self.polyCount = materialInfo.PolyCount()
        self.polyOffset = materialInfo.PolyOffset()
        self.shUnk3 = materialInfo.ShUnk3()
        self.materialName = materialInfo.MaterialName()
        self.shUnk4 = materialInfo.ShUnk4()

    # MaterialInfoT
    def Pack(self, builder):
        if self.materialName is not None:
            materialName = builder.CreateString(self.materialName)
        MaterialInfoStart(builder)
        MaterialInfoAddPolyCount(builder, self.polyCount)
        MaterialInfoAddPolyOffset(builder, self.polyOffset)
        MaterialInfoAddShUnk3(builder, self.shUnk3)
        if self.materialName is not None:
            MaterialInfoAddMaterialName(builder, materialName)
        MaterialInfoAddShUnk4(builder, self.shUnk4)
        materialInfo = MaterialInfoEnd(builder)
        return materialInfo
