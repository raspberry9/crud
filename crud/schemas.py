# from datetime import datetime

# from sqlalchemy import Integer, String, DateTime, Boolean
# from sqlalchemy.sql.schema import Column

# from crud.database import Base


# class User(Base):
#     __tablename__ = 'users'

#     user_id = Column(Integer, primary_key=True)
#     username = Column(String, nullable=False)
#     email = Column(String, nullable=False)
#     password = Column(String, nullable=False)
#     created_at = Column(DateTime, default=datetime.now)
#     updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
#     is_active = Column(Boolean, default=True)
