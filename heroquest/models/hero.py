from enum import Enum

from sqlalchemy.orm import Mapped, mapped_column

from .. import db


class HeroClass(Enum):
    BARBARIAN = "barbarian"
    DWARF = "dwarf"
    ELF = "elf"
    WIZARD = "wizard"


class Hero(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    hero_class: Mapped[HeroClass] = mapped_column()
    body: Mapped[int] = mapped_column()
    mind: Mapped[int] = mapped_column()
    attack: Mapped[int] = mapped_column()
    defend: Mapped[int] = mapped_column()
    movement: Mapped[int] = mapped_column()
