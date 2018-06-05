from django.urls import path
from cms import views
from django.conf.urls import url
# from cms.views import FoodListView


app_name = 'cms'
urlpatterns = [
    url(r'food/$', views.food_search, name='food_list'),   # 食材表 FoodListView.as_view()
    url(r'user/$', views.search, name='user_search'),   # ユーザー検索用

    # インデックス
    path('map010/', views.index, name='index'),   # 300件表示
    path('map020/', views.index_new, name='index_new'),   # デバイス最新情報
    path('map030/', views.index_sea, name='index_sea'),   # デバイス動向確認
    path('map030/&#3f;deviceid=<deviceid>', views.index_sea, name='index_search'),   # デバイス動向確認

    # メニュー
    path('menu/', views.menu, name='menu'),   # メニュー

    # 資産
    path('asset/', views.asset_list, name='asset_list'),   # 一覧
    path('asset/sea/', views.asset_list, name='asset_sea'),   # 検索
    path('asset/add/', views.asset_edit, name='asset_add'),   # 登録
    path('asset/mod/<asset_id>/', views.asset_edit, name='asset_mod'),   # 修正
    path('asset/del/<asset_id>/', views.asset_del, name='asset_del'),   # 削除
    path('asset/csv_export/', views.csv_export, name='csv_export'),   # CSVダウンロード

    # 倉庫
    path('warehouse/', views.warehouse_list, name='warehouse_list'),  # 一覧
    path('warehouse/add/', views.warehouse_edit, name='warehouse_add'),  # 登録
    path('warehouse/mod/<warehouse_id>/', views.warehouse_edit, name='warehouse_mod'),  # 修正
    path('warehouse/del/<warehouse_id>/', views.warehouse_del, name='warehouse_del'),  # 削除


]