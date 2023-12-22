from app import db, app
from sqlalchemy import Integer, String, Column, Float, ForeignKey
from sqlalchemy.orm import relationship


class Category(db.Model):
    __tablename__ = 'category'

    # thuoctinh
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

    # relationship vs product
    products = relationship('Product', backref='category', lazy=True)


class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    with app.app_context():
        # db.create_all()
        # c1 = Category(name="Mobile")
        # c2 = Category(name="Tablet")
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()

        p1 = Product(name='iphone 13', price=20000000, category_id=1,
                     image="https://i.ebayimg.com/images/g/QL0AAOSwzh9h2~v1/s-l960.png")
        p2 = Product(name='galaxy s23', price=23000000, category_id=2,
                     image="https://i.ebayimg.com/images/g/qfUAAOSwHSdh2~vr/s-l960.png")
        p3 = Product(name='iphone 13', price=15000000, category_id=1,
                     image="https://i.ebayimg.com/images/g/qfUAAOSwHSdh2~vr/s-l960.png")
        p4 = Product(name='ipad pro 10', price=31000000, category_id=2,
                     image="https://i.ebayimg.com/images/g/U94AAOSwLiFh2~vy/s-l960.png")
        p5 = Product(name='galaxy a12', price=28000000, category_id=2,
                     image="https://i.ebayimg.com/images/g/drYAAOSwSsdh2~v5/s-l960.png")

        db.session.add_all([p1, p2, p3, p4, p5])
        db.session.commit()