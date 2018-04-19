from django.db.models import Q
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Zhaopin, Category, WorkLocation
from utils import custom_paginator
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from users.models import Candidaters, Recruiter
from .forms import add_zhaopinForm
from django.contrib import messages


# Create your views here.

def index(request):
    try:
        mark = int(request.session['mark'])
    except:
        mark = None
        # 求职者
    if mark == 0:
        u_id = request.session.get('id')
        cand = Candidaters.objects.get(id=u_id)
        # 招聘
    if mark == 1:
        u_id = request.session.get('id')
        rec = Recruiter.objects.get(id=u_id)

    keywords = request.GET.get('keywords')
    zhaopin_list = Zhaopin.objects.all().order_by('-publishTime')[:10]
    category_list = Category.objects.all()
    workLocation_list = WorkLocation.objects.all()
    if not keywords:
        keywords = ''
    return render(request, 'index.html', locals())


def detail(request, pk):
    category_list = Category.objects.filter(~Q(name=''))
    workLocation_list = WorkLocation.objects.all()
    workLocation_list1 = workLocation_list[:9]
    workLocation_list2 = workLocation_list[9:]

    zhaopin = Zhaopin.objects.get(pk=pk)
    job_content_list = zhaopin.content.split('\n')
    return render(request, 'zhaopin/detail.html', locals())


def social(request):
    zhaopin_list = Zhaopin.objects.all().order_by('-publishTime')[:10]
    zhaopin_list1 = zhaopin_list[:5]
    zhaopin_list2 = zhaopin_list[5:10]
    workLocation_list = WorkLocation.objects.all()
    category_list = Category.objects.filter(~Q(name=''))
    return render(request, 'zhaopin/social.html', locals())


class SearchView(ListView):
    model = Zhaopin
    template_name = 'zhaopin/search.html'
    context_object_name = 'zhaopin_list'

    def get_queryset(self):
        keywords = self.request.GET.get('keywords') or ''
        workLocation_id = self.request.GET.get('lid') or 0
        category_id = self.request.GET.get('tid') or 0

        workLocation_id = int(workLocation_id)
        category_id = int(category_id)

        # 搜索关键词
        if keywords and not workLocation_id and not category_id:
            zhaopin_list = super().get_queryset().filter(
                (Q(title__contains=keywords) | Q(content__contains=keywords))
            ).order_by('-publishTime')
        # 工作地筛选
        elif workLocation_id and not category_id:
            zhaopin_list = super().get_queryset().filter(workLocation_id=workLocation_id).order_by('-publishTime')
        # 职位分类筛选
        elif category_id and not workLocation_id:
            zhaopin_list = super().get_queryset().filter(category_id=category_id).order_by('-publishTime')
        # 工作地/职位分类一起筛选
        elif workLocation_id and category_id:
            zhaopin_list = super().get_queryset().filter(
                Q(workLocation_id=workLocation_id) & Q(category_id=category_id)).order_by(
                '-publishTime')
        # 工作地/职位分类/关键词一起筛选
        elif keywords and workLocation_id and category_id:
            zhaopin_list = super().get_queryset().filter(
                (Q(title__contains=keywords) | Q(content__contains=keywords)) & Q(workLocation_id=workLocation_id) & Q(
                    category_id=category_id)
            ).order_by('-publishTime')
        # 无条件搜索
        else:
            zhaopin_list = super().get_queryset().all().order_by('-publishTime')

        self.zhaopin_list = zhaopin_list
        self.workLocation_id = workLocation_id
        self.category_id = category_id
        self.keywords = keywords
        return self.zhaopin_list, self.workLocation_id, self.category_id, self.keywords

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = Paginator(self.zhaopin_list, 10)
        page = self.request.GET.get('page', 1)
        page_range = paginator.page_range
        zhaopin_list = paginator.page(page)
        list_num = paginator.count

        start, end = custom_paginator(int(page), len(page_range), 10)
        page_range = range(start, end + 1)
        # 获取所有的工作地和分类
        category_list = Category.objects.filter(~Q(name=''))
        workLocation_list = WorkLocation.objects.all()
        workLocation_list1 = workLocation_list[:9]
        workLocation_list2 = workLocation_list[9:]

        context.update({
            'list_num': list_num,
            'page_range': page_range,
            'zhaopin_list': zhaopin_list,
            'workLocation_id': self.workLocation_id,
            'category_id': self.category_id,
            'keywords': self.keywords,
            'category_list': category_list,
            'workLocation_list1': workLocation_list1,
            'workLocation_list2': workLocation_list2
        })
        return context


def add_zhaopin(request):
    if request.method == 'POST':
        form = add_zhaopinForm(request.POST)
        if form.is_valid():
            author_id = request.session['id']
            form.cleaned_data['author_id'] = author_id
            Zhaopin.objects.create(**form.cleaned_data)
            messages.success(request, '招聘岗位发布成功!')
            return redirect(reverse('zhaopin:add_zhaopin'))
    else:
        form = add_zhaopinForm()
        return render(request, 'zhaopin/add_zhaopin.html', locals())
