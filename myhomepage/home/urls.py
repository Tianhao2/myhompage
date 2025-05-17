from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index'),

    # 🇯🇵 日文页面
    path('about/', lambda r: views.render_page(r, 'about.html'), name='about'),
    path('contact/', lambda r: views.contact(r, 'contact.html'), name='contact'),
    path('services/', lambda r: views.render_page(r, 'services.html'), name='services'),
    path('portfolio/', lambda r: views.render_page(r, 'portfolio.html'), name='portfolio'),
    path('portfolio-details1/', lambda r: views.render_page(r, 'portfolio-details1.html')),
    path('portfolio-details2/', lambda r: views.render_page(r, 'portfolio-details2.html')),
    path('portfolio-details3/', lambda r: views.render_page(r, 'portfolio-details3.html')),
    path('portfolio-details4/', lambda r: views.render_page(r, 'portfolio-details4.html')),
    path('portfolio-details5/', lambda r: views.render_page(r, 'portfolio-details5.html')),
    path('recruit/', lambda r: views.render_page(r, 'recruit.html'), name='recruit'),

    # 🇨🇳 中文页面
    path('cn/', lambda r: views.render_page(r, 'index_cn.html'), name='index_cn'),
    path('cn/about/', lambda r: views.render_page(r, 'about_cn.html')),
    path('cn/contact/', lambda r: views.contact(r, 'contact_cn.html'), name='contact_cn'),
    path('cn/services/', lambda r: views.render_page(r, 'services_cn.html')),
    path('cn/portfolio/', lambda r: views.render_page(r, 'portfolio_cn.html')),
    path('cn/portfolio-details1/', lambda r: views.render_page(r, 'portfolio-details1_cn.html')),
    path('cn/portfolio-details2/', lambda r: views.render_page(r, 'portfolio-details2_cn.html')),
    path('cn/portfolio-details3/', lambda r: views.render_page(r, 'portfolio-details3_cn.html')),
    path('cn/portfolio-details4/', lambda r: views.render_page(r, 'portfolio-details4_cn.html')),
    path('cn/portfolio-details5/', lambda r: views.render_page(r, 'portfolio-details5_cn.html')),
    path('cn/recruit/', lambda r: views.render_page(r, 'recruit_cn.html')),
]