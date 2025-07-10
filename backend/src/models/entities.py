from sqlalchemy.orm import mapped_column


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    
    preferences: Mapped["UserPreferences"] = relationship("UserPreferences", back_populates="user", uselist=False)
    activities: Mapped[list["ActivityHistory"]] = relationship("ActivityHistory", back_populates="user")
    recommendations: Mapped[list["Recommendation"]] = relationship("Recommendation", back_populates="user")



class Activity(Base):
    __tablename__ = 'activities'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(ForeignKey('users.id'))
    description: Mapped[str] = mapped_column(Text)


class ActivityHistory(Base):
    __tablename__ = "activity_historys"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    activity_id: Mapped[int] = mapped_column(ForeignKey("activities.id"))
    timestamp: Mapped[DateTime] = mapped_column(DateTime)
    
    user: Mapped["User"] = relationship("User", back_populates="activities")
    activity: Mapped["Activity"] = relationship("Activity")


class UserPreferences(Base):
    __tablename__ = 'user_preferences'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    preference_data: Mapped[str] = mapped_column(Text)
    user: Mapped["User"] = relationship("User", back_populates="preferences")



class Recommendation(Base):
    __tablename__ = 'recommendations'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    activity_id: Mapped[int] = mapped_column(ForeignKey("activities.id"))
    reason: Mapped[str] = mapped_column(Text)

    user: Mapped["User"] = relationship("User", back_populates="recommendations")
    activity: Mapped["Activity"] = relationship("Activity")
