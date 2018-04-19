from django.shortcuts import render, HttpResponse, redirect, reverse
from django.http import HttpResponseRedirect

from users import models
from .forms import RecRegisterForm, CanRegisterForm
from django.contrib import messages
from .models import Recruiter, Candidaters
from .models import set_password, check_password_hash
from resume.forms import ResumeForm
from resume.models import Resume, Resume_relationship
from zhaopin.models import Zhaopin


# Create your views here.


def register_can(request):
    if request.method == 'POST':
        form = CanRegisterForm(request.POST, request.FILES)
        # 数据提交是否合法
        if form.is_valid():
            username = form.cleaned_data['username']
            # 用户名已存在,返回注册页面
            if len(Candidaters.objects.filter(username=username)) != 0:
                # messages.info(request, '用户名已存在!')
                info = {'error': '用户名已存在!'}
                return render(request, 'users/register.html', info)
            else:
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    # messages.info(request, '两次密码输入不一致!')
                    info = {'error': '两次密码输入不一致!'}
                    return render(request, 'users/register.html', info)
                else:
                    # 加密放在了model里进行操作
                    form.save()
                    messages.success(request, '注册成功!')
                    return HttpResponseRedirect('/index')
    else:
        form = CanRegisterForm()
    return render(request, 'users/register.html', locals())


def register_rec(request):
    if request.method == 'POST':
        form = RecRegisterForm(request.POST, request.FILES)
        # 数据提交是否合法
        if form.is_valid():
            username = form.cleaned_data['username']
            # 用户名已存在,返回注册页面
            if len(Recruiter.objects.filter(username=username)) != 0:
                messages.error(request, '用户名已存在!')
                return render(request, 'users/register.html', locals())
            else:
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if password1 != password2:
                    messages.error(request, '两次密码输入不一致!')
                    return render(request, 'users/register.html', locals())
                else:
                    # 加密放在了model里进行操作
                    form.save()
                    messages.success(request, '注册成功!')
                    return HttpResponseRedirect('/index')
    else:
        form = RecRegisterForm()
    return render(request, 'users/register.html', locals())


def login_can(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 检查用户是否存在
        cand = Candidaters.objects.filter(username=username).first()
        # 用户不存在
        if cand == None:
            messages.error(request, '用户名或密码错误!')
            return render(request, 'users/login_cand.html', locals())
        password1 = cand.password1
        # 校验密码是否正确
        # 密码错误
        if not check_password_hash(password, password1):
            messages.error(request, '用户名或密码错误!')
            return render(request, 'users/login_cand.html', locals())

        request.session['username'] = cand.username
        request.session['id'] = cand.id
        request.session['mark'] = 0
        messages.success(request, '登录成功!')
        return HttpResponseRedirect('/index')
    return render(request, 'users/login_cand.html', locals())


def login_rec(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        department = request.POST.get('department')

        # 检查用户是否存在
        rec = Recruiter.objects.filter(username=username).first()
        # 用户不存在
        if rec == None:
            messages.error(request, '用户名或密码错误!')
            return render(request, 'users/login_rec.html', locals())
        password1 = rec.password1
        # 校验密码是否正确
        # 密码错误
        if not check_password_hash(password, password1):
            messages.error(request, '用户名或密码错误!')
            return render(request, 'users/login_rec.html', locals())
        # 部门名不正确
        if department != rec.department:
            messages.error(request, '用户名或密码错误!')
            return render(request, 'users/login_rec.html', locals())
        request.session['username'] = rec.username
        request.session['id'] = rec.id
        request.session['mark'] = 1
        messages.success(request, '登录成功!')
        return HttpResponseRedirect('/index')
    return render(request, 'users/login_rec.html', locals())


def logout(request):
    request.session.flush()
    return redirect(reverse('zhaopin:index'))


def edit_info_cand(request, id):
    cand = Candidaters.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        headshot = request.FILES.get('headshot') or 'default.jpg'
        models.Candidaters.objects.filter(id=id).update(username=username,
                                                        email=email, headshot=headshot, tel=tel)
        # info = {'message': '修改成功!'}
        messages.success(request, '修改成功!')
        return HttpResponseRedirect('/users/edit_info_cand/%s' % id, )
    return render(request, 'candidaters/can_info_edit.html', locals())


def edit_resume_cand(request, id):
    resume = Resume.objects.filter(user_id=id).first()
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        if form.is_valid():
            try:
                # 修改简历
                form.save()
                messages.success(request, '简历修改成功!')
            except:
                # 创建简历
                form.cleaned_data['user_id'] = int(id)
                Resume.objects.create(**form.cleaned_data)
                messages.success(request, '简历创建成功!')
    else:
        form = ResumeForm(instance=resume)
    return render(request, 'candidaters/can_resume_edit.html', locals())


def edit_info_rec(request, id):
    rec = Recruiter.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        department = request.POST.get('department')
        models.Recruiter.objects.filter(id=id).update(username=username,
                                                      email=email, department=department, tel=tel)
        messages.success(request, '修改成功!')
        return HttpResponseRedirect('/users/edit_info_rec/%s' % id, )
    return render(request, 'recruiter/rec_info_edit.html', locals())


def resume_list(request):
    try:
        rec_id = int(request.session['id'])
        resume_id_list = Resume_relationship.objects.filter(rec_id=rec_id)
        resume_list = [Resume.objects.filter(id=resume_id.resume_id)[0] for resume_id in resume_id_list]
        # 去重
        resume_list = set(resume_list)
    except:
        info = '暂无投递简历!'
    return render(request, 'recruiter/rec_resume_list.html', locals())


# 已投递的招聘岗位
def send_zhaopin_list(request):
    try:
        # 候选人id
        cand_id = int(request.session['id'])
        # 候选人对应简历
        resume = Resume.objects.filter(user_id=cand_id).first()
        # 候选人投递的岗位
        zhaopin_id_list = Resume_relationship.objects.filter(resume_id=resume.id)
        zhaopin_list = [Zhaopin.objects.filter(id=zhaopin_id.zhaopin_id)[0] for zhaopin_id in zhaopin_id_list]
    except:
        info = '还未投递简历,赶紧去看看吧'
    return render(request, 'candidaters/send_zhaopin_list.html', locals())


def zhaopin_detail(request, id):
    return HttpResponseRedirect('/detail/%s/' % id)
