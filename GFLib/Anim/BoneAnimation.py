# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Anim

import flatbuffers
from flatbuffers.compat import import_numpy

from GFLib.Anim.BoneInit import BoneInitT, BoneInit
from GFLib.Anim.BoneTrack import BoneTrackT, BoneTrack

np = import_numpy()

class BoneAnimation(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = BoneAnimation()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsBoneAnimation(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # BoneAnimation
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # BoneAnimation
    def Tracks(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            obj = BoneTrack()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # BoneAnimation
    def TracksLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # BoneAnimation
    def TracksIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # BoneAnimation
    def InitData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            obj = BoneInit()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def BoneAnimationStart(builder):
    builder.StartObject(2)

def Start(builder):
    BoneAnimationStart(builder)

def BoneAnimationAddTracks(builder, tracks):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(tracks), 0)

def AddTracks(builder, tracks):
    BoneAnimationAddTracks(builder, tracks)

def BoneAnimationStartTracksVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartTracksVector(builder, numElems):
    return BoneAnimationStartTracksVector(builder, numElems)

def BoneAnimationAddInitData(builder, initData):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(initData), 0)

def AddInitData(builder, initData):
    BoneAnimationAddInitData(builder, initData)

def BoneAnimationEnd(builder):
    return builder.EndObject()

def End(builder):
    return BoneAnimationEnd(builder)

try:
    from typing import List, Optional
except:
    pass

class BoneAnimationT(object):

    # BoneAnimationT
    def __init__(self):
        self.tracks = None  # type: List[BoneTrackT]
        self.initData = None  # type: Optional[BoneInitT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        boneAnimation = BoneAnimation()
        boneAnimation.Init(buf, pos)
        return cls.InitFromObj(boneAnimation)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, boneAnimation):
        x = BoneAnimationT()
        x._UnPack(boneAnimation)
        return x

    # BoneAnimationT
    def _UnPack(self, boneAnimation):
        if boneAnimation is None:
            return
        if not boneAnimation.TracksIsNone():
            self.tracks = []
            for i in range(boneAnimation.TracksLength()):
                if boneAnimation.Tracks(i) is None:
                    self.tracks.append(None)
                else:
                    boneTrack_ = BoneTrackT.InitFromObj(boneAnimation.Tracks(i))
                    self.tracks.append(boneTrack_)
        if boneAnimation.InitData() is not None:
            self.initData = BoneInitT.InitFromObj(boneAnimation.InitData())

    # BoneAnimationT
    def Pack(self, builder):
        if self.tracks is not None:
            trackslist = []
            for i in range(len(self.tracks)):
                trackslist.append(self.tracks[i].Pack(builder))
            BoneAnimationStartTracksVector(builder, len(self.tracks))
            for i in reversed(range(len(self.tracks))):
                builder.PrependUOffsetTRelative(trackslist[i])
            tracks = builder.EndVector()
        if self.initData is not None:
            initData = self.initData.Pack(builder)
        BoneAnimationStart(builder)
        if self.tracks is not None:
            BoneAnimationAddTracks(builder, tracks)
        if self.initData is not None:
            BoneAnimationAddInitData(builder, initData)
        boneAnimation = BoneAnimationEnd(builder)
        return boneAnimation
