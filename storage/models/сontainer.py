from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from storage.mixins import PkMixin
from storage.models import BaseModel


class Container(BaseModel, PkMixin):
    __tablename__ = "container"
    container_name: Mapped[str] = mapped_column(
        String(length=256), nullable=False, unique=True
    )
    description: Mapped[str] = mapped_column(String(1024), nullable=True)

    parent_container_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("container.id"), nullable=True
    )
    parent_container: Mapped["Container"] = relationship(
        "Container", remote_side=[id], back_populates="child_containers"
    )
    items = relationship("Item", back_populates="container")

    def __str__(self):
        return self.container_name
