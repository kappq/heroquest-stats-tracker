from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .. import db
from .hero import Hero


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
    heroes: Mapped[list[Hero]] = relationship()
