from django.contrib import admin
from .models import SurveyResponse


@admin.register(SurveyResponse)
class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = (
        'category', 'name', 'email', 'created_at'
    )  # 显示哪些字段为列表列
    list_filter = (
        'category', 'name'
    )  # 右侧过滤器
    search_fields = ('name', 'email', 'category')  # 上方搜索栏可搜索字段
    ordering = ('-created_at',)  # 默认排序方式：最新提交在上

    # 可选：只读字段
    readonly_fields = ('created_at',)

    # 可选：显示字段顺序（点击进去查看详情页时）
    fields = (
        'category', 'name', 'email',
        'q1', 'q2', 'q3', 'q4', 'q5',
        'q6', 'q7', 'q8', 'q9', 'q10',
        'created_at',
    )
