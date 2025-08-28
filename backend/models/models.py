from datetime import datetime, timezone
from db.db import db
import uuid


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
    user_role = db.Column(db.Integer, nullable=False)
    profile_image_path = db.Column(db.String(300))

    is_verified = db.Column(db.Boolean, nullable=False, default=False)
    verification_sent_at = db.Column(db.DateTime)

    # Relações
    player_profile = db.relationship(
        "PlayerProfile",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan",
    )


class PlayerProfile(db.Model):
    __tablename__ = "player_profile"

    user_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )

    # Relações
    user = db.relationship("User", back_populates="player_profile")
    characters = db.relationship(
        "PlayerCharacter", back_populates="player", cascade="all, delete-orphan"
    )
    master_profile = db.relationship(
        "MasterProfile",
        back_populates="player",
        uselist=False,
        cascade="all, delete-orphan",
    )


class PlayerCharacter(db.Model):
    __tablename__ = "player_characters"

    character_id = db.Column(
        db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    player_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("player_profile.user_id", ondelete="CASCADE"),
        nullable=False,
    )

    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer)
    char_class = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    background = db.Column(db.String(100), nullable=False)
    alignement = db.Column(db.String(100), nullable=False)
    total_health = db.Column(db.Integer, default=0)
    current_health = db.Column(db.Integer, default=0)
    armor_class = db.Column(db.Integer, default=0)
    initiative = db.Column(db.Integer, default=0)
    speed = db.Column(db.Integer, default=0)
    strength = db.Column(db.Integer, default=0)
    dexterity = db.Column(db.Integer, default=0)
    constitution = db.Column(db.Integer, default=0)
    intelligence = db.Column(db.Integer, default=0)
    wisdom = db.Column(db.Integer, default=0)
    charisma = db.Column(db.Integer, default=0)

    # Relações
    player = db.relationship("PlayerProfile", back_populates="characters")
    inventory = db.relationship(
        "Inventory", back_populates="character", cascade="all, delete-orphan"
    )
    languages = db.relationship(
        "Language", back_populates="character", cascade="all, delete-orphan"
    )
    skills = db.relationship(
        "Skill", back_populates="character", cascade="all, delete-orphan"
    )
    spells = db.relationship(
        "Spell", back_populates="character", cascade="all, delete-orphan"
    )


class Inventory(db.Model):
    __tablename__ = "inventory"
    inv_id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("player_characters.character_id", ondelete="CASCADE"),
        nullable=False,
    )
    weight = db.Column(db.Integer, default=0)
    item = db.Column(db.String(100))
    description = db.Column(db.Text)
    character = db.relationship("PlayerCharacter", back_populates="inventory")


class Language(db.Model):
    __tablename__ = "languages"
    lang_id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("player_characters.character_id", ondelete="CASCADE"),
        nullable=False,
    )
    known_language = db.Column(db.String(100))
    character = db.relationship("PlayerCharacter", back_populates="languages")


class Skill(db.Model):
    __tablename__ = "skills"
    skill_id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("player_characters.character_id", ondelete="CASCADE"),
        nullable=False,
    )
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    character = db.relationship("PlayerCharacter", back_populates="skills")


class Spell(db.Model):
    __tablename__ = "spells"
    spell_id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    character_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("player_characters.character_id", ondelete="CASCADE"),
        nullable=False,
    )
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    character = db.relationship("PlayerCharacter", back_populates="spells")


class MasterProfile(db.Model):
    __tablename__ = "master_profile"
    master_id = db.Column(db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    player_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("player_profile.user_id", ondelete="CASCADE"),
        nullable=False,
    )
    began_at = db.Column(db.Date, nullable=False)

    # Relações
    player = db.relationship("PlayerProfile", back_populates="master_profile")
    characters = db.relationship(
        "MasterCharacter", back_populates="master", cascade="all, delete-orphan"
    )


class MasterCharacter(db.Model):
    __tablename__ = "master_characters"
    character_id = db.Column(
        db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    master_id = db.Column(
        db.UUID(as_uuid=True),
        db.ForeignKey("master_profile.master_id", ondelete="CASCADE"),
        nullable=False,
    )

    name = db.Column(db.String(100), nullable=False)
    level = db.Column(db.Integer)
    char_class = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    background = db.Column(db.String(100), nullable=False)
    alignement = db.Column(db.String(100), nullable=False)
    total_health = db.Column(db.Integer, default=0)
    current_health = db.Column(db.Integer, default=0)
    armor_class = db.Column(db.Integer, default=0)
    initiative = db.Column(db.Integer, default=0)
    speed = db.Column(db.Integer, default=0)
    strength = db.Column(db.Integer, default=0)
    dexterity = db.Column(db.Integer, default=0)
    constitution = db.Column(db.Integer, default=0)
    intelligence = db.Column(db.Integer, default=0)
    wisdom = db.Column(db.Integer, default=0)
    charisma = db.Column(db.Integer, default=0)
    boss = db.Column(db.Integer, default=0)
    experience = db.Column(db.Integer, default=0)

    # Relação
    master = db.relationship("MasterProfile", back_populates="characters")
