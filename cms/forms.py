from django.forms import ModelForm
from cms.models import Asset, Warehouse


class AssetForm(ModelForm):
    """資産のフォーム"""
    class Meta:
        model = Asset
        fields = ('id', 'Name', 'Warehouse', )   # 記述可能領域の設定


class WarehouseForm(ModelForm):
    """倉庫のフォーム"""
    class Meta:
        model = Warehouse
        fields = ('id', 'Warehouse_Name', )

