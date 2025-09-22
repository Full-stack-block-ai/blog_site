from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

# Define User model, inherits from db.Model for database mapping
class User(db.Model):
    # Primary key column, string type
    id: so.Mapped[str] = so.mapped_column(primary_key=True)
    # Username column, string (64 chars), indexed, unique
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    # Email column, string (120 chars), indexed, unique
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    # Password hash column, string (256 chars), can be None
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return '<user {}>'.format(self.username)