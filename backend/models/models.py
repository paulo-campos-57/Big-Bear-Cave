from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import uuid

from db.db import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.string(100), unique=True, nullable=False)
    email = db.Column(db.string(100), unique=True, nullable=False)
    password = db.Column(db.string(50), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    user_role = db.Column(db.Numeric(10, 2))
