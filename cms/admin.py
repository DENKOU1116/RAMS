from django.contrib import admin
from cms.models import Warehouse, Asset, Place, Device

# admin.site.register(Warehouse)
# admin.site.register(Asset)


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'Warehouse_Name', )   # 一覧に出したい項目
    list_display_links = ('id', 'Warehouse_Name', )   # 修正リンクでクリックできる項目
    ordering = ['id', ]   # ソートの順番


admin.site.register(Warehouse, WarehouseAdmin)


class AssetAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Warehouse',)
    list_display_links = ('id', 'Name', 'Warehouse',)
    raw_id_fields = ('Warehouse',)   # 外部キーをプルダウンにしない（データ件数が増加時のタイムアウトを予防）
    ordering = ['id', 'Warehouse', ]


admin.site.register(Asset, AssetAdmin)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'division', 'address', 'point', 'multip', 'multils', 'multipo', 'geometryc', )
    list_display_links = ('id', 'name', 'division', 'address', 'point', 'multip', 'multils', 'multipo', 'geometryc', )
    ordering = ['name', ]


admin.site.register(Place, PlaceAdmin)


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'time', 'deviceid', 'latitude', 'longitude', 'radius', 'source', )
    list_display_links = ('id', 'time', 'deviceid', 'latitude', 'longitude', 'radius', 'source', )


admin.site.register(Device, DeviceAdmin)

# Register your models here.
