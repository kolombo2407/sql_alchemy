from fastapi import FastAPI, HTTPException, Depends
from typing import List
from loguru import logger

from database import SessionLocal
from schema import UserGet, PostGet, FeedGet
from table_feed import Feed
from table_post import Post
from table_user import User

from sqlalchemy.orm import Session
from sqlalchemy.sql import func

app = FastAPI()


def get_db():
    with SessionLocal() as db:
        return db


@app.get("/user/{id}", response_model=UserGet)
def get_user(id, db: Session = Depends(get_db)):
    result = db.query(User).filter(User.id == id).one_or_none()
    if result:
        return result
    else:
        raise HTTPException(404, 'User not found')


@app.get("/post/{id}", response_model=PostGet)
def get_user(id, db: Session = Depends(get_db)):
    result = db.query(Post).filter(Post.id == id).one_or_none()
    if result:
        return result
    else:
        raise HTTPException(404, 'Post not found')


@app.get("/user/{id}/feed", response_model=List[FeedGet])
def get_user_feed(id, limit: int = 10, db: Session = Depends(get_db)):
    result = (
        db.query(Feed)
        .filter(Feed.user_id == id)
        .order_by(Feed.time.desc())
        .limit(limit)
        .all()
    )
    logger.info(result)
    return result


@app.get("/post/{id}/feed", response_model=List[FeedGet])
def get_feed_post(id, limit: int = 10, db: Session = Depends(get_db)):
    result = (
        db.query(Feed)
        .filter(Feed.post_id == id)
        .order_by(Feed.time.desc())
        .limit(limit)
        .all()
    )
    logger.info(result)
    return result


@app.get("/post/recommendations/{limit}", response_model=List[PostGet])
def get_recommendations(id: int, limit: int = 10, db: Session = Depends(get_db)):
    result = (
        db.query(Post)
        .limit(limit)
        .order_by(Post.id.desc())
        .all()
    )
    logger.info(result)
    return result

