import csv
# import operator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from io import StringIO
# from django.views.generic.list import ListView
# from django.db.models import Q
from cms.models import Asset, Warehouse, Device, Food
from cms.forms import AssetForm, WarehouseForm
from django.views.decorators.csrf import csrf_protect
# from django.db.models import Max
from django.contrib.auth.models import User
from django.shortcuts import render
from .filters import UserFilter, FoodFilter, IndexFilter


@login_required
@csrf_protect
def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'cms/user_list.html', {'filter': user_filter})


@login_required
@csrf_protect
def index(request):
    """デバイスのデータ"""
    devices = Device.objects.all().order_by('-time')
    return render(request, 'cms/index.html', {'devices': devices})


@login_required
@csrf_protect
def index_sea(request, device_deviceid=None):
    """デバイスの動向"""
    if device_deviceid:
        index_list = Device.objects.all().order_by('-time')
        index_filter = IndexFilter(request.GET, queryset=index_list)
    else:
        index_list = Device.objects.all().order_by('-time')
        index_filter = IndexFilter(request.GET, queryset=index_list)
    return render(request, 'cms/index_sea.html', {'filter': index_filter})
    # if device_deviceid:
    #     dvs = Device.objects.all().filter(deviceid='deviceid').order_by('id')
    #     devices = Device.objects.all().values('deviceid').distinct()
    # else:
    #     dvs = Device()
    #     devices = Device.objects.all().values('deviceid').distinct()
    # return render(request, 'cms/index_sea.html', {'devices': devices, 'dvs': dvs})


@login_required
@csrf_protect
def index_new(request):
    """デバイスの最新情報"""
    devices = Device.objects.all().order_by('deviceid', '-time').distinct('deviceid')
    assets = Asset.objects.all()
    return render(request, 'cms/index_new.html', {'devices': devices, 'assets': assets })


@login_required
@csrf_protect
def menu(request):
    return render(request, 'cms/menu.html')


@login_required
@csrf_protect
def asset_list(request):
    """資産の一覧"""
#    return HttpResponse('資産の一覧')
#     if asset_id:  # asset_idが指定されている（検索時）
#         assets = Asset.objects.all().filter(asset_id='asset_id').order_by('id')
#     else:  # asset_idが指定されていない（一覧表示時）
    assets = Asset.objects.all().order_by('id')

    return render(request,
                  'cms/asset_list.html',   # 使用するテンプレート
                  {'assets': assets})   # テンプレートに渡すデータ


@login_required
@csrf_protect
def asset_edit(request, asset_id=None):
    """資産の編集"""
#    return HttpResponse('資産の編集')
    if asset_id:   # asset_idが指定されている（修正時）
        asset = get_object_or_404(Asset, pk=asset_id)
    else:   # asset_idが指定されていない（追加時）
        asset = Asset()

    if request.method == 'POST':
        form = AssetForm(request.POST, instance=asset)   # POSTをrequestし、インスタンスからフォームを作成
        if form.is_valid():   # フォームのバリデーション
            asset = form.save(commit=False)
            asset.save()
            return redirect('cms:asset_list')
    else:   # GET のとき
        form = AssetForm(instance=asset)   # assetインスタンスからフォームを作成
    return render(request, 'cms/asset_edit.html', dict(form=form, asset_id=asset_id))


@login_required
@csrf_protect
def asset_del(request, asset_id):
    """資産の削除"""
    # return HttpResponse('資産の削除')
    asset = get_object_or_404(Asset, pk=asset_id)
    asset.delete()
    return redirect('cms:asset_list')


@login_required
@csrf_protect
def csv_export(request):
    memory_file = StringIO()   # メモリファイルにString型のIOの元を入れた
    writer = csv.writer(memory_file)   # writerにcsvの内容をメモリファイルを用いて挿入
    for asset in Asset.objects.all().order_by('id'):   # Assetの全てでforループ
        row = [asset.pk, asset.Name, asset.Warehouse]   # rowに行の内容を挿入
        writer.writerow(row)   # writerを用いてrowの値を入れる。
    response = HttpResponse(
        memory_file.getvalue(), content_type='text/csv', charset="shift-jis")
    response['Content-Disposition'] = 'attachment; filename=asset_'"now()"'.csv'
    return response


def warehouse_list(request):
    return request


# @login_required
# class warehouse_list(ListView):
#     """倉庫の一覧"""
#     context_object_name = 'warehouses'
#     paginate_by = 2   # 1ページは最大2件ずつでページングする。
#     template_name = 'cms/warehouse_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(warehouse_list, self).get_context_data(**kwargs)
#         warehouses = Warehouse.objects.all()
#         context['warehouses'] = warehouses
#         return context


@login_required
@csrf_protect
def warehouse_edit(request, warehouse_id=None):
    """倉庫の編集"""
    if warehouse_id:   # warehouse_idが指定されている（修正時）
        warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    else:   # warehouse_idが指定されていない（追加時）
        warehouse = Warehouse()

    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=warehouse)   # POSTされたrequestデータからフォーム作成
        if form.is_valid():   # フォームのバリデーション
            warehouse = form.save(commit=False)
            warehouse.save()
            return redirect('cms:warehouse_list')
        else:   # GETのとき
            form = WarehouseForm(instance=warehouse)   # warehouseインスタンスからフォームを作成
        return render(request, 'cms/warehouse_edit.html', dict(form=form, warehouse_id=warehouse_id))


@login_required
@csrf_protect
def warehouse_del(request, asset_id, warehouse_id):
    """倉庫の削除"""
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    warehouse.delete()
    return redirect('cms:warehouse_list', asset_id=asset_id)


# class FoodListView(ListView):
#     model = Food
#     paginate_by = 2
#     context_object_name = 'food_list'
#     template_name = 'cms/food_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(FoodListView, self).get_context_data(**kwargs)
#
#         # 絞り込み条件の設定
#         kinds = Kind.objects.all()
#         context['kinds'] = kinds
#
#         return context
#
#
# def get_queryset(self):
#     # デフォルトは全件取得
#     results = self.model.objects.all()
#
#     # GETのURLクエリパラメータを取得する
#     # 該当のクエリパラメータが存在しない場合は、[]が返ってくる
#     q_kinds = self.request.GET.getlist('kind')
#     q_name = self.request.GET.get('name')
#
#     # 品種での絞込は、Kind.pkとして存在してる値のみ対象とする
#     # "a"とかを指定するとValueErrorになるため
#     if len(q_kinds) != 0:
#         kinds = [x for x in q_kinds if x in ["1", "2"]]
#         results = results.filter(kind__in=kinds)
#
#     # 名前での絞り込み
#     if q_name is not None:
#         results = results.filter(name__contains=q_name)
#
#     return results


@login_required
@csrf_protect
def food_search(request):
    food_list = Food.objects.all()
    food_filter = FoodFilter(request.GET, queryset=food_list)
    return render(request, 'cms/food_list.html', {'filter': food_filter})

# Create your views here.
