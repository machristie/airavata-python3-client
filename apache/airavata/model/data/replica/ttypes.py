#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys

from thrift.transport import TTransport


class ReplicaLocationCategory(object):
    GATEWAY_DATA_STORE = 0
    COMPUTE_RESOURCE = 1
    LONG_TERM_STORAGE_RESOURCE = 2
    OTHER = 3

    _VALUES_TO_NAMES = {
        0: "GATEWAY_DATA_STORE",
        1: "COMPUTE_RESOURCE",
        2: "LONG_TERM_STORAGE_RESOURCE",
        3: "OTHER",
    }

    _NAMES_TO_VALUES = {
        "GATEWAY_DATA_STORE": 0,
        "COMPUTE_RESOURCE": 1,
        "LONG_TERM_STORAGE_RESOURCE": 2,
        "OTHER": 3,
    }


class ReplicaPersistentType(object):
    TRANSIENT = 0
    PERSISTENT = 1

    _VALUES_TO_NAMES = {
        0: "TRANSIENT",
        1: "PERSISTENT",
    }

    _NAMES_TO_VALUES = {
        "TRANSIENT": 0,
        "PERSISTENT": 1,
    }


class DataProductType(object):
    FILE = 0
    COLLECTION = 1

    _VALUES_TO_NAMES = {
        0: "FILE",
        1: "COLLECTION",
    }

    _NAMES_TO_VALUES = {
        "FILE": 0,
        "COLLECTION": 1,
    }

# TODO: manually modified file so that this comes BEFORE DataProductModel
class DataReplicaLocationModel(object):
    """
    Attributes:
     - replicaId
     - productUri
     - replicaName
     - replicaDescription
     - creationTime
     - lastModifiedTime
     - validUntilTime
     - replicaLocationCategory
     - replicaPersistentType
     - storageResourceId
     - filePath
     - replicaMetadata
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'replicaId', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'productUri', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'replicaName', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'replicaDescription', 'UTF8', None, ),  # 4
        (5, TType.I64, 'creationTime', None, None, ),  # 5
        (6, TType.I64, 'lastModifiedTime', None, None, ),  # 6
        (7, TType.I64, 'validUntilTime', None, None, ),  # 7
        (8, TType.I32, 'replicaLocationCategory', None, None, ),  # 8
        (9, TType.I32, 'replicaPersistentType', None, None, ),  # 9
        (10, TType.STRING, 'storageResourceId', 'UTF8', None, ),  # 10
        (11, TType.STRING, 'filePath', 'UTF8', None, ),  # 11
        (12, TType.MAP, 'replicaMetadata', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 12
    )

    def __init__(self, replicaId=None, productUri=None, replicaName=None, replicaDescription=None, creationTime=None, lastModifiedTime=None, validUntilTime=None, replicaLocationCategory=None, replicaPersistentType=None, storageResourceId=None, filePath=None, replicaMetadata=None,):
        self.replicaId = replicaId
        self.productUri = productUri
        self.replicaName = replicaName
        self.replicaDescription = replicaDescription
        self.creationTime = creationTime
        self.lastModifiedTime = lastModifiedTime
        self.validUntilTime = validUntilTime
        self.replicaLocationCategory = replicaLocationCategory
        self.replicaPersistentType = replicaPersistentType
        self.storageResourceId = storageResourceId
        self.filePath = filePath
        self.replicaMetadata = replicaMetadata

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.replicaId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.productUri = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.replicaName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.replicaDescription = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.creationTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.lastModifiedTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.validUntilTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.replicaLocationCategory = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I32:
                    self.replicaPersistentType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.STRING:
                    self.storageResourceId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.STRING:
                    self.filePath = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.MAP:
                    self.replicaMetadata = {}
                    (_ktype17, _vtype18, _size16) = iprot.readMapBegin()
                    for _i20 in range(_size16):
                        _key21 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val22 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.replicaMetadata[_key21] = _val22
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('DataReplicaLocationModel')
        if self.replicaId is not None:
            oprot.writeFieldBegin('replicaId', TType.STRING, 1)
            oprot.writeString(self.replicaId.encode('utf-8') if sys.version_info[0] == 2 else self.replicaId)
            oprot.writeFieldEnd()
        if self.productUri is not None:
            oprot.writeFieldBegin('productUri', TType.STRING, 2)
            oprot.writeString(self.productUri.encode('utf-8') if sys.version_info[0] == 2 else self.productUri)
            oprot.writeFieldEnd()
        if self.replicaName is not None:
            oprot.writeFieldBegin('replicaName', TType.STRING, 3)
            oprot.writeString(self.replicaName.encode('utf-8') if sys.version_info[0] == 2 else self.replicaName)
            oprot.writeFieldEnd()
        if self.replicaDescription is not None:
            oprot.writeFieldBegin('replicaDescription', TType.STRING, 4)
            oprot.writeString(self.replicaDescription.encode('utf-8') if sys.version_info[0] == 2 else self.replicaDescription)
            oprot.writeFieldEnd()
        if self.creationTime is not None:
            oprot.writeFieldBegin('creationTime', TType.I64, 5)
            oprot.writeI64(self.creationTime)
            oprot.writeFieldEnd()
        if self.lastModifiedTime is not None:
            oprot.writeFieldBegin('lastModifiedTime', TType.I64, 6)
            oprot.writeI64(self.lastModifiedTime)
            oprot.writeFieldEnd()
        if self.validUntilTime is not None:
            oprot.writeFieldBegin('validUntilTime', TType.I64, 7)
            oprot.writeI64(self.validUntilTime)
            oprot.writeFieldEnd()
        if self.replicaLocationCategory is not None:
            oprot.writeFieldBegin('replicaLocationCategory', TType.I32, 8)
            oprot.writeI32(self.replicaLocationCategory)
            oprot.writeFieldEnd()
        if self.replicaPersistentType is not None:
            oprot.writeFieldBegin('replicaPersistentType', TType.I32, 9)
            oprot.writeI32(self.replicaPersistentType)
            oprot.writeFieldEnd()
        if self.storageResourceId is not None:
            oprot.writeFieldBegin('storageResourceId', TType.STRING, 10)
            oprot.writeString(self.storageResourceId.encode('utf-8') if sys.version_info[0] == 2 else self.storageResourceId)
            oprot.writeFieldEnd()
        if self.filePath is not None:
            oprot.writeFieldBegin('filePath', TType.STRING, 11)
            oprot.writeString(self.filePath.encode('utf-8') if sys.version_info[0] == 2 else self.filePath)
            oprot.writeFieldEnd()
        if self.replicaMetadata is not None:
            oprot.writeFieldBegin('replicaMetadata', TType.MAP, 12)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.replicaMetadata))
            for kiter23, viter24 in self.replicaMetadata.items():
                oprot.writeString(kiter23.encode('utf-8') if sys.version_info[0] == 2 else kiter23)
                oprot.writeString(viter24.encode('utf-8') if sys.version_info[0] == 2 else viter24)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

class DataProductModel(object):
    """
    Attributes:
     - productUri
     - gatewayId
     - parentProductUri
     - productName
     - productDescription
     - ownerName
     - dataProductType
     - productSize
     - creationTime
     - lastModifiedTime
     - productMetadata
     - replicaLocations
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'productUri', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'gatewayId', 'UTF8', None, ),  # 2
        (3, TType.STRING, 'parentProductUri', 'UTF8', None, ),  # 3
        (4, TType.STRING, 'productName', 'UTF8', None, ),  # 4
        (5, TType.STRING, 'productDescription', 'UTF8', None, ),  # 5
        (6, TType.STRING, 'ownerName', 'UTF8', None, ),  # 6
        (7, TType.I32, 'dataProductType', None, None, ),  # 7
        (8, TType.I32, 'productSize', None, None, ),  # 8
        (9, TType.I64, 'creationTime', None, None, ),  # 9
        (10, TType.I64, 'lastModifiedTime', None, None, ),  # 10
        (11, TType.MAP, 'productMetadata', (TType.STRING, 'UTF8', TType.STRING, 'UTF8', False), None, ),  # 11
        (12, TType.LIST, 'replicaLocations', (TType.STRUCT, (DataReplicaLocationModel, DataReplicaLocationModel.thrift_spec), False), None, ),  # 12
    )

    def __init__(self, productUri=None, gatewayId=None, parentProductUri=None, productName=None, productDescription=None, ownerName=None, dataProductType=None, productSize=None, creationTime=None, lastModifiedTime=None, productMetadata=None, replicaLocations=None,):
        self.productUri = productUri
        self.gatewayId = gatewayId
        self.parentProductUri = parentProductUri
        self.productName = productName
        self.productDescription = productDescription
        self.ownerName = ownerName
        self.dataProductType = dataProductType
        self.productSize = productSize
        self.creationTime = creationTime
        self.lastModifiedTime = lastModifiedTime
        self.productMetadata = productMetadata
        self.replicaLocations = replicaLocations

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.productUri = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.gatewayId = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.parentProductUri = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.productName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.productDescription = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.ownerName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I32:
                    self.dataProductType = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I32:
                    self.productSize = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.I64:
                    self.creationTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 10:
                if ftype == TType.I64:
                    self.lastModifiedTime = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 11:
                if ftype == TType.MAP:
                    self.productMetadata = {}
                    (_ktype1, _vtype2, _size0) = iprot.readMapBegin()
                    for _i4 in range(_size0):
                        _key5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        _val6 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.productMetadata[_key5] = _val6
                    iprot.readMapEnd()
                else:
                    iprot.skip(ftype)
            elif fid == 12:
                if ftype == TType.LIST:
                    self.replicaLocations = []
                    (_etype10, _size7) = iprot.readListBegin()
                    for _i11 in range(_size7):
                        _elem12 = DataReplicaLocationModel()
                        _elem12.read(iprot)
                        self.replicaLocations.append(_elem12)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('DataProductModel')
        if self.productUri is not None:
            oprot.writeFieldBegin('productUri', TType.STRING, 1)
            oprot.writeString(self.productUri.encode('utf-8') if sys.version_info[0] == 2 else self.productUri)
            oprot.writeFieldEnd()
        if self.gatewayId is not None:
            oprot.writeFieldBegin('gatewayId', TType.STRING, 2)
            oprot.writeString(self.gatewayId.encode('utf-8') if sys.version_info[0] == 2 else self.gatewayId)
            oprot.writeFieldEnd()
        if self.parentProductUri is not None:
            oprot.writeFieldBegin('parentProductUri', TType.STRING, 3)
            oprot.writeString(self.parentProductUri.encode('utf-8') if sys.version_info[0] == 2 else self.parentProductUri)
            oprot.writeFieldEnd()
        if self.productName is not None:
            oprot.writeFieldBegin('productName', TType.STRING, 4)
            oprot.writeString(self.productName.encode('utf-8') if sys.version_info[0] == 2 else self.productName)
            oprot.writeFieldEnd()
        if self.productDescription is not None:
            oprot.writeFieldBegin('productDescription', TType.STRING, 5)
            oprot.writeString(self.productDescription.encode('utf-8') if sys.version_info[0] == 2 else self.productDescription)
            oprot.writeFieldEnd()
        if self.ownerName is not None:
            oprot.writeFieldBegin('ownerName', TType.STRING, 6)
            oprot.writeString(self.ownerName.encode('utf-8') if sys.version_info[0] == 2 else self.ownerName)
            oprot.writeFieldEnd()
        if self.dataProductType is not None:
            oprot.writeFieldBegin('dataProductType', TType.I32, 7)
            oprot.writeI32(self.dataProductType)
            oprot.writeFieldEnd()
        if self.productSize is not None:
            oprot.writeFieldBegin('productSize', TType.I32, 8)
            oprot.writeI32(self.productSize)
            oprot.writeFieldEnd()
        if self.creationTime is not None:
            oprot.writeFieldBegin('creationTime', TType.I64, 9)
            oprot.writeI64(self.creationTime)
            oprot.writeFieldEnd()
        if self.lastModifiedTime is not None:
            oprot.writeFieldBegin('lastModifiedTime', TType.I64, 10)
            oprot.writeI64(self.lastModifiedTime)
            oprot.writeFieldEnd()
        if self.productMetadata is not None:
            oprot.writeFieldBegin('productMetadata', TType.MAP, 11)
            oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.productMetadata))
            for kiter13, viter14 in self.productMetadata.items():
                oprot.writeString(kiter13.encode('utf-8') if sys.version_info[0] == 2 else kiter13)
                oprot.writeString(viter14.encode('utf-8') if sys.version_info[0] == 2 else viter14)
            oprot.writeMapEnd()
            oprot.writeFieldEnd()
        if self.replicaLocations is not None:
            oprot.writeFieldBegin('replicaLocations', TType.LIST, 12)
            oprot.writeListBegin(TType.STRUCT, len(self.replicaLocations))
            for iter15 in self.replicaLocations:
                iter15.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


