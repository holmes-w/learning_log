from django.contrib import admin
from learning_logs.models import Topic, Entry
# Register your models here.
# 账户：admin  密码：w@123456
admin.site.register(Topic)
admin.site.register(Entry)