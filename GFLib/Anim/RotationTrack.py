# automatically generated by the FlatBuffers compiler, do not modify
from GFLib.Anim.DynamicRotationTrack import DynamicRotationTrackT
from GFLib.Anim.FixedRotationTrack import FixedRotationTrackT
from GFLib.Anim.Framed16RotationTrack import Framed16RotationTrackT
from GFLib.Anim.Framed8RotationTrack import Framed8RotationTrackT


# namespace: Anim

class RotationTrack(object):
    NONE = 0
    FixedRotationTrack = 1
    DynamicRotationTrack = 2
    Framed16RotationTrack = 3
    Framed8RotationTrack = 4

def RotationTrackCreator(unionType, table):
    from flatbuffers.table import Table
    if not isinstance(table, Table):
        return None
    if unionType == RotationTrack().FixedRotationTrack:
        return FixedRotationTrackT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == RotationTrack().DynamicRotationTrack:
        return DynamicRotationTrackT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == RotationTrack().Framed16RotationTrack:
        return Framed16RotationTrackT.InitFromBuf(table.Bytes, table.Pos)
    if unionType == RotationTrack().Framed8RotationTrack:
        return Framed8RotationTrackT.InitFromBuf(table.Bytes, table.Pos)
    return None
