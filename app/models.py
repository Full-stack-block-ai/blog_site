from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

# Define User model, inherits from db.Model for database mapping
class User(UserMixin, db.Model):
    # Primary key column, string type
    id: so.Mapped[str] = so.mapped_column(primary_key=True)
    # Username column, string (64 chars), indexed, unique
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    # Email column, string (120 chars), indexed, unique
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    # Password hash column, string (256 chars), can be None
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    #posts relationship
    posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates='author')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<user {}>'.format(self.username)
    
# Define Post model, inherits from db.Model for database mapping
class Post(db.Model):
    #Primary Key column, string type
    id: so.Mapped[str] = so.mapped_column(primary_key=True)
    # body column, string (64 chars), indexed, unique
    body: so.Mapped[str] = so.mapped_column(sa.String(140))
    #timestamp column
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    #user id column
    user_id:so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    #author relationship
    author: so.Mapped[User] = so.relationship(back_populates='posts')

    def __repr__(self):
        '<post{}>'.format(self.body)
