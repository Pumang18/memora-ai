from datetime import datetime, timezone

from sqlalchemy import (
    String,
    Text,
    Integer,
    Float,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


def utc_now():
    return datetime.now(timezone.utc)


class Conversation(Base):

    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        default="New Conversation"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now
    )


class Message(Base):

    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("conversations.id"),
        index=True
    )

    role: Mapped[str] = mapped_column(
        String(20)
    )

    content: Mapped[str] = mapped_column(
        Text
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now
    )


class Memory(Base):

    __tablename__ = "memories"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("conversations.id"),
        index=True
    )

    memory_type: Mapped[str] = mapped_column(
        String(50)
    )

    content: Mapped[str] = mapped_column(
        Text
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now
    )


class APIUsage(Base):

    __tablename__ = "api_usage"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    conversation_id: Mapped[int] = mapped_column(
        ForeignKey("conversations.id"),
        index=True
    )

    model: Mapped[str] = mapped_column(
        String(100)
    )

    input_tokens: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    output_tokens: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    total_tokens: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    estimated_cost_usd: Mapped[float | None] = mapped_column(
        Float,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=utc_now
    )