from django.shortcuts import render
from users.models import Recruiter, Candidaters
from zhaopin.models import Zhaopin, Category
from django.db.models import Q
import json


def histogram(request):
    id = request.session['id']
    # 确认招聘者
    rec = Recruiter.objects.filter(id=id).first()
    # 获取招聘信息所有分类
    Categories = Category.objects.filter(~Q(name=''))
    # 该招聘者发布的所有招聘信息
    zhaopin_list = Zhaopin.objects.filter(author=rec)
    # 获取每个分类的招聘信息数量
    nums = [len(zhaopin_list.filter(category=cate)) for cate in Categories]
    Categories = [cate.name for cate in Categories]
    myjson = {
        'type': 'column',
        'colorByPoint': 'true',
        'name': '岗位分类',
        'data': nums,
        'showInLegend': 'true'
    }
    data = json.dumps(myjson)
    return render(request, 'recruiter/rec_statics.html', locals())


def line(request):
    id = request.session['id']
    # 确认招聘者
    rec = Recruiter.objects.filter(id=id).first()
    # 该招聘者发布的所有招聘信息
    zhaopin_list = Zhaopin.objects.filter(author=rec)
    # 岗位按时间分类
    dates = zhaopin_list.dates('publishTime', 'month')
    # 每个月发布的数量
    datas = [len(zhaopin_list.filter(publishTime__year=date.year,
                                     publishTime__month=date.month)) for date in dates]
    # 拼接字符串: 2017-9
    # 月份分类列表
    categories = [(str(date.year) + '-' + str(date.month)) for date in dates]
    myjson = {
        'name': '月增岗位数量',
        'data': datas
    }
    series = json.dumps(myjson)
    return render(request, 'recruiter/rec_lines.html', locals())
