from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from users.models import Candidaters
from zhaopin.models import Zhaopin
from django.contrib import messages
from resume.models import Resume, Resume_relationship
from .forms import ResumeForm


# Create your views here.
def send_resume(request, id):
    uid = request.session.get('id', None)
    if uid == None:
        messages.info(request, '请先登录再投递简历!')
        return HttpResponseRedirect('/users/login_can')
    # 招聘岗位id
    zhaopin_id = int(id)
    if request.session['mark'] == 0:
        # 候选人id
        cand_id = request.session['id']
        # 简历id
        resume = Resume.objects.filter(user_id=cand_id).first()
        resume_id = resume.id
        # 发布岗位者id
        zhaopin = Zhaopin.objects.filter(id=zhaopin_id).first()
        rec_id = zhaopin.author.id
        # 判断是否重复投递
        is_send = Resume_relationship.objects.filter(resume_id=resume_id, zhaopin_id=zhaopin_id, rec_id=rec_id).first()
        if is_send:
            messages.error(request, '请不要重复投递简历!')
        else:
            Resume_relationship.objects.create(resume_id=resume_id, zhaopin_id=zhaopin_id, rec_id=rec_id)
            messages.success(request, '简历投递成功!')
    else:
        messages.error(request, '身份不符,不能投递简历!')
    return HttpResponseRedirect('/detail/%d' % zhaopin_id)


def resume_detail(request, id):
    resume = Resume.objects.filter(id=id).first()
    form = ResumeForm(instance=resume)
    return render(request, 'recruiter/resume_detail.html', locals())
