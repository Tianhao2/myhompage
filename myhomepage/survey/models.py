from django.db import models

class SurveyResponse(models.Model):
    category = models.CharField("课程类别", max_length=100, default="")  # AWS / MuleSoft / Salesforce 等，从URL自动写入
    name = models.CharField("姓名", max_length=100, default="")
    email = models.EmailField("邮箱", default="")

    q1 = models.TextField("问题1：您对课程内容的满意度？", default="")
    q2 = models.TextField("问题2：授课老师是否清晰易懂？", default="")
    q3 = models.TextField("问题3：学习节奏是否合适？", default="")
    q4 = models.TextField("问题4：课程材料是否充分？", default="")
    q5 = models.TextField("问题5：练习内容是否有帮助？", default="")
    q6 = models.TextField("问题6：您希望增加哪些内容？", default="")
    q7 = models.TextField("问题7：对本次课程的总体评分？", default="")
    q8 = models.TextField("问题8：参加该课程的动机？", default="")
    q9 = models.TextField("问题9：对组织方式的意见或建议？", default="")
    q10 = models.TextField("问题10：未来还希望开设哪些主题？", default="")

    created_at = models.DateTimeField("提交时间", auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.category} ({self.created_at.strftime('%Y-%m-%d')})"
