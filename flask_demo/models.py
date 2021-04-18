

from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""

    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间



# 单独设置自增id
author_book = db.Table(
    'tbl_author_book',
    db.Column('id',db.Integer, primary_key=True),
    db.Column('author_id',db.Integer, db.ForeignKey('tbl_author.id')),
    db.Column("book_id", db.Integer, db.ForeignKey('tbl_book.id')),
)


# # 设置联合主键
# author_book = db.Table(
#     'tbl_author_book',
#     db.Column('author_id',db.Integer, db.ForeignKey('tbl_author.id', ),primary_key=True),
#     db.Column("book_id",db.Integer, db.ForeignKey('tbl_book.id'),primary_key=True),
# )

class Author(db.Model, BaseModel):
    __tablename__ = 'tbl_author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
    gender = db.Column(db.Boolean)
    books = db.relationship('Book',secondary=author_book,backref=db.backref('authors')) # Book是表名，secondary表示多对多中通过第三张表去查找


class Book(db.Model, BaseModel):
    __tablename__ = 'tbl_book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    price = db.Column(db.Float)
    publish_id = db.Column(db.Integer, db.ForeignKey('tbl_publish.id'))


    def __repr__(self):  # 自定义显示，类似django里的__str__
        return self.name
class Publish(db.Model, BaseModel):
    __tablename__ = 'tbl_publish'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    addr = db.Column(db.String(128))

    # # 参数含义：
    # 第一个参数：Book，代表Publish.books 是从Book表里面去查询
    # 第二个参数: backref,是为了类似django那样反向查询Book.publish
    books = db.relationship('Book', backref='publish')   # 为了能够像django那样使用Publish.books来查询

"""
python main.py db init 
python main.py db migrate  # 类似django的 makermigrations ，即生成迁移文件
python main.py db upgrade  # 类似django的 migrate，提交迁移到数据库

"""