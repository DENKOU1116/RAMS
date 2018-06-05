# from django.db import models
import pytz
from django.contrib.gis.db import models
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin


class TimezoneMiddleware(MiddlewareMixin):
    def process_request(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()


class Warehouse(models.Model):
    """倉庫"""
    id = models.CharField('倉庫コード', max_length=20, primary_key=True)   # ID
    Warehouse_Name = models.CharField('倉庫', max_length=50)   # 倉庫名

    def __str__(self):
        return self.Warehouse_Name


class Asset(models.Model):
    """資産"""
    id = models.CharField('ID', max_length=20, primary_key=True)   # ID
    Name = models.CharField('名前', max_length=50)   # 資産名
    Warehouse = models.ForeignKey(Warehouse, verbose_name='倉庫', related_name='assets', on_delete=models.CASCADE)   # 倉庫

    def __str__(self):
        return self.Name


class Place(models.Model):
    """場所"""
    id = models.CharField('ID', max_length=20, primary_key=True)
    name = models.CharField('名前', max_length=50, )   # 場所名
    division = models.CharField('区分', max_length=1, choices=(('1', '倉庫'), ('2', '店舗')), default=2, )   # 区分
    address = models.CharField('住所', max_length=100, )   # 住所
    point = models.PointField('地点', null=True, blank=True, )
    # length = models.IntegerField('半径', max_length=20, )
    # Geomet = models.GeometryField('Geometry', null=True, blank=True, )
    # LineStr = models.LineStringField('LineString', null=True, blank=True, )
    # Poly = models.PolygonField('Polygon', null=True, blank=True, )
    multip = models.MultiPointField('MultiPoint', null=True, blank=True, )
    multils = models.MultiLineStringField('MultiLineString', null=True, blank=True, )
    multipo = models.MultiPolygonField('MultiPolygon', null=True, blank=True, )
    geometryc = models.GeometryCollectionField('GeometryCollection', null=True, blank=True, )

    def __str__(self):
        return self.name


class Device(models.Model):
    """デバイス位置情報"""
    time = models.DateTimeField('時間', default=timezone.datetime.now, )
    deviceid = models.CharField('デバイスID', max_length=6, )
    latitude = models.FloatField('緯度', )
    longitude = models.FloatField('経度', )
    radius = models.IntegerField('半径', )
    source = models.CharField('種類', max_length=10, )

    def __str__(self):
        return self.deviceid


# class Distance(models.Model):
#     """住所情報"""
#     code = models.CharField('都道府県コード', max_length=5, )
#     prefecture = models.CharField('都道府県名', max_length=10, )
#     ci_code = models.CharField('市区町村コード', max_length=10, )
#     city = models.CharField('市区町村名', max_length=50, )
#     ch_code = models.CharField('大字町丁目コード', max_length=50, )
#     chome = models.CharField('大字町丁目名', max_length=50, )
#     latitude = models.FloatField('緯度', )
#     longitude = models.FloatField('経度', )
#     o_code = models.IntegerField('原典資料コード', )
#     c_code = models.IntegerField('大字･字･丁目区分コード', )
#
#     def __str__(self):
#         return self.code


class Kind(models.Model):
    name = models.CharField('Name', max_length=255)


class Food(models.Model):
    kind = models.ForeignKey(Kind, verbose_name="品種", on_delete=models.CASCADE)
    name = models.CharField('名前', max_length=255)

    def __str__(self):
        return self.name

# Create your models here.
