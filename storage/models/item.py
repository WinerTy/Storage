from enum import Enum as PyEnum
from typing import TYPE_CHECKING

from sqlalchemy import String, Enum, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from storage.mixins import PkMixin
from storage.models import BaseModel

if TYPE_CHECKING:
    from .сontainer import Container


class ItemStatus(str, PyEnum):
    taken = "taken"
    stored = "stored"
    ended = "ended"


class Item(BaseModel, PkMixin):
    __tablename__ = "item"

    item_name: Mapped[str] = mapped_column(String(256), nullable=False)
    status: Mapped[str] = mapped_column(
        Enum(ItemStatus),
        nullable=False,
        default=ItemStatus.stored,
        server_default=ItemStatus.stored.value,
    )
    description: Mapped[str] = mapped_column(String(1024), nullable=True)

    container_id: Mapped[int] = mapped_column(Integer, ForeignKey("container.id"))
    container: Mapped["Container"] = relationship("Container", back_populates="items")
    count: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
