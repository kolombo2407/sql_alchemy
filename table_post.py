from sqlalchemy import Column, Integer, String

from database import Base, SessionLocal


class Post(Base):
    __tablename__ = 'post'
    __tableargs__ = {'schema': 'public'}
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)


# if __name__ == '__main__':
#     session = SessionLocal()
#     result = (
#         session.query(Post)
#         .filter(Post.topic == 'business')
#         .order_by(Post.id.desc())
#         .limit(10)
#         .all()
#     )
#     print([i.id for i in result])
