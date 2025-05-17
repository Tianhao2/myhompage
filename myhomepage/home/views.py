from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from intelligentbrainhp.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER

from django.http import JsonResponse
from django.utils.translation import gettext as _

import smtplib
import ssl
import certifi
from email.message import EmailMessage


def send_custom_email(subject, body, from_email, to_email):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    context = ssl.create_default_context(cafile=certifi.where())

    with smtplib.SMTP("smtp.lolipop.jp", 587) as server:
        server.starttls(context=context)
        server.login(from_email, EMAIL_HOST_PASSWORD)
        server.send_message(msg)

def contact(request, template_name):
    if request.method == 'POST':
        # 获取表单数据
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()
        
        # 验证必填字段
        if not all([name, email, subject, message]):
            return JsonResponse({
                'success': False,
                'message': _('すべての必須フィールドに入力してください。')
            }, status=400)
        
        # 验证邮箱格式
        if '@' not in email:
            return JsonResponse({
                'success': False,
                'message': _('有効なメールアドレスを入力してください。')
            }, status=400)
        
        try:
            send_custom_email(subject, message, EMAIL_HOST_USER, EMAIL_HOST_USER)
        except Exception as e:
                return JsonResponse({
                    'success': False,
                    'message': _('メッセージ送信中にエラーが発生しました。後ほど再試行してください。')
                }, status=500)        
        return JsonResponse({'success': True})
    
    # GET 请求：渲染空白表单页面
    return render(request, template_name)

# 通用页面视图
def render_page(request, template_name):
    return render(request, template_name)

# 可选：设定默认首页
def index(request):
    return render(request, 'index.html')
