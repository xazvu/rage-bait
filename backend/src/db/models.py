from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, Text, DateTime, ForeignKey, Float, Boolean, Column
from datetime import datetime
from sqlalchemy import Table, MetaData

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    role: Mapped[str] = mapped_column(String(20), default="user")  # user/moderator
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now)

    preferences: Mapped["UserPreferences"] = relationship("UserPreferences", back_populates="user", uselist=False)
    activities_history: Mapped[list["ActivityHistory"]] = relationship("ActivityHistory", back_populates="user")
    recommendations: Mapped[list["Recommendation"]] = relationship("Recommendation", back_populates="user")
    favorites: Mapped[list["Activity"]] = relationship("Activity", secondary="favorites", back_populates="favorited_by")


class Activity(Base):
    __tablename__ = 'activities'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(String(50))
    mod: Mapped[str] = mapped_column(String(200))
    timestamp: Mapped[str] = mapped_column(String(20))
    budget: Mapped[float] = mapped_column(Float)
    date_of_activity: Mapped[datetime] = mapped_column(DateTime)
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # is_approved: Mapped[bool] = mapped_column(Boolean, default=False)

    favorited_by: Mapped[list["User"]] = relationship("User", secondary="favorites", back_populates="favorites")
    activity_histories: Mapped[list["ActivityHistory"]] = relationship("ActivityHistory", back_populates="activity")
    recommendations: Mapped[list["Recommendation"]] = relationship("Recommendation", back_populates="activity")
    photos: Mapped[list["ActivityPhoto"]] = relationship("ActivityPhoto", back_populates="activity")


class ActivityPhoto(Base):
    __tablename__ = 'activity_photos'

    id: Mapped[int] = mapped_column(primary_key=True)
    activity_id: Mapped[int] = mapped_column(ForeignKey("activities.id"))
    url: Mapped[str] = mapped_column(String(255))
    is_main: Mapped[bool] = mapped_column(Boolean, default=False)
    activity: Mapped["Activity"] = relationship("Activity", back_populates="photos")


class UserPreferences(Base):
    __tablename__ = 'user_preferences'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
    mood: Mapped[str] = mapped_column(String(50))
    available_time: Mapped[int] = mapped_column(Integer)  # в минутах
    budget: Mapped[float] = mapped_column(Float)
    location: Mapped[str] = mapped_column(String(100))
    preference_data: Mapped[str] = mapped_column(Text)  # Дополнительные настройки (JSON)

    user: Mapped["User"] = relationship("User", back_populates="preferences")


class ActivityHistory(Base):
    __tablename__ = "activity_history"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    activity_id: Mapped[int] = mapped_column(ForeignKey("activities.id"))
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    rating: Mapped[int] = mapped_column(Integer)  # 1-5 звезд
    review: Mapped[str] = mapped_column(Text)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)

    user: Mapped["User"] = relationship("User", back_populates="activities_history")
    activity: Mapped["Activity"] = relationship("Activity", back_populates="activity_histories")


class Recommendation(Base):
    __tablename__ = 'recommendations'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    activity_id: Mapped[int] = mapped_column(ForeignKey("activities.id"))
    reason: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    user: Mapped["User"] = relationship("User", back_populates="recommendations")
    activity: Mapped["Activity"] = relationship("Activity", back_populates="recommendations")


favorites = Table(
    "favorites",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("activity_id", ForeignKey("activities.id"), primary_key=True)
)

