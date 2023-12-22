from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models import Category, Product

# MUỐN TẠO 1 PAGE K DÍNH TỚI MODEL TH IMPORT BASEVIEW và expose
admin = Admin(app=app, name=" QUẢN TRỊ BÁN HÀNG", template_mode='bootstrap4')


class MyProductView(ModelView):
    column_list = ['id', 'name', 'price']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['price']
    column_editable_list = ['name', 'price']


class MyCategoryView(ModelView):
    column_list = ['name', 'products']


class StatsView(BaseView):
    @expose("/")
    def __index__(self):
        return self.render('admin/stats.html')


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))

admin.add_view(StatsView(name="THỐNG KÊ BÁO CÁO"))