# stdlib
from typing import Any
from typing import Optional

# third party
from google.protobuf.reflection import GeneratedProtocolMessageType

# syft relative
from ... import deserialize
from ... import serialize
from ...core.common import UID
from ...core.common.serde.serializable import bind_protobuf
from ...proto.lib.python.slice_pb2 import Slice as Slice_PB
from .primitive_factory import PrimitiveFactory
from .primitive_interface import PyPrimitive
from .types import SyPrimitiveRet


@bind_protobuf
class Slice(PyPrimitive):
    def __init__(
        self,
        start: Any = None,
        stop: Any = None,
        step: Optional[Any] = None,
        id: Optional[UID] = None,
    ):
        # first, second, third
        if stop is None and step is None:
            # slice treats 1 arg as stop not start
            stop = start
            start = None

        self.value = slice(start, stop, step)
        self._id: UID = id if id else UID()

    @property
    def id(self) -> UID:
        """We reveal PyPrimitive.id as a property to discourage users and
        developers of Syft from modifying .id attributes after an object
        has been initialized.

        :return: returns the unique id of the object
        :rtype: UID
        """
        return self._id

    def __eq__(self, other: Any) -> SyPrimitiveRet:
        res = self.value.__eq__(other)
        return PrimitiveFactory.generate_primitive(value=res)

    def __ge__(self, other: Any) -> SyPrimitiveRet:
        res = self.value.__ge__(other)  # type: ignore
        return PrimitiveFactory.generate_primitive(value=res)

    def __gt__(self, other: Any) -> SyPrimitiveRet:
        res = self.value.__gt__(other)  # type: ignore
        return PrimitiveFactory.generate_primitive(value=res)

    def __le__(self, other: Any) -> SyPrimitiveRet:
        res = self.value.__le__(other)  # type: ignore
        return PrimitiveFactory.generate_primitive(value=res)

    def __lt__(self, other: Any) -> SyPrimitiveRet:
        res = self.value.__lt__(other)  # type: ignore
        return PrimitiveFactory.generate_primitive(value=res)

    def __ne__(self, other: Any) -> SyPrimitiveRet:
        res = self.value.__ne__(other)
        return PrimitiveFactory.generate_primitive(value=res)

    def __repr__(self) -> str:
        return self.value.__repr__()

    def __str__(self) -> str:
        return self.value.__str__()

    def indices(self, index: int) -> tuple:
        res = self.value.indices(index)
        return PrimitiveFactory.generate_primitive(value=res)

    @property
    def start(self) -> Optional[int]:
        return self.value.start

    @property
    def step(self) -> Optional[int]:
        return self.value.step

    @property
    def stop(self) -> Optional[int]:
        return self.value.stop

    def upcast(self) -> slice:
        return self.value

    def _object2proto(self) -> Slice_PB:
        return Slice_PB(
            start=self.start,
            stop=self.stop,
            step=self.step,
            id=serialize(obj=self._id),
        )

    @staticmethod
    def _proto2object(proto: Slice_PB) -> "Slice":
        id_: UID = deserialize(blob=proto.id)

        return Slice(
            start=proto.start,
            stop=proto.stop,
            step=proto.step,
            id=id_,
        )

    @staticmethod
    def get_protobuf_schema() -> GeneratedProtocolMessageType:
        return Slice_PB
