from . import sql
from flask import request
from flask_demo.models import Author,Publish,Book, author_book
from flask_demo import db

@sql.route('/create')
def create():
    author = Author(name='arvin',age=25,gender=True)
    author2 = Author(name='alex',age=25,gender=True)
    # db.session.add(author)
    # db.session.commit()

    pub = Publish(name='北京',addr='北京',)
    pub2 = Publish(name='shanghai',addr='北京',)

    # db.session.add(pub)
    # db.session.commit()

    book = Book(name="python入门", price=3.14,publish_id=pub.id)
    book2 = Book(name="python高级", price=3.14,publish_id=pub.id)
    author.books.append(book)  # 为多对多表添加数据
    db.session.add_all([author,pub,book,book2,author2,pub2])  # 一次增加多条
    db.session.commit()



    return 'ok'

@sql.route('/query')
def query():

    books = Book.query.all()  # 查询所有
    print(books)
    print(Book.query.first().name) # 获取第一条
    book1 = Book.query.get(1) # 获取id为1的记录
    print(book1.name)

    # 下面两个查询是同样的结果
    print(Book.query.filter_by(name='python高级').first().name)
    print(Book.query.filter(Book.name=="python高级").first().name)

    # 或查询
    from sqlalchemy import or_
    ret=Book.query.filter(or_(Book.name=="python高级", Book.name.endswith('1'))).all()
    print(ret)

    # 排序
    print(Book.query.order_by(Book.id).all())
    print(Book.query.order_by(Book.id.desc()).all())


    # 分组
    from sqlalchemy import func
    print(db.session.query(Book.publish_id,func.count(Book.publish_id)).group_by(Book.publish_id).all())
    return 'ok'


@sql.route('update')
def update_delete():
    # 更新
    # book=Book.query.get(1)
    # book.name='python入入门'
    # db.session.add(book)
    # db.session.commit()

    # 批量更新
    Book.query.filter(Book.id==2).update({'name':"PYTHON"})
    db.session.commit()

    # 删除

    book = Book.query.get(3)
    db.session.delete(book)
    db.session.commit()
    return 'ok'