from sqlalchemy import Column, Integer, String
from sqlalchemy.sql import func, select

from database import Base, SessionLocal


class User(Base):
    __tablename__ = 'user'
    __tableargs__ = {'schema': 'public'}
    id = Column(Integer, primary_key=True)
    gender = Column(Integer)
    age = Column(Integer)
    country = Column(String)
    city = Column(String)
    exp_group = Column(Integer)
    os = Column(String)
    source = Column(String)


# if __name__ == '__main__':
#     session = SessionLocal()
#     result = (
#         session.query(User.country, User.os, func.count('*').label('cnt'))
#         .filter(User.exp_group == 3)
#         .group_by(User.country, User.os)
#         .having(func.count('*') > 100)
#         .order_by(func.count('*').desc())
#         .all()
#     )
#     print([(i.country, i.os, i.cnt) for i in result])
