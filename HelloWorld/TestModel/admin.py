# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Test, Contact, Tag
#无需变为TestModel.models

# Register your models here.

# 内联样式
class TagInline(admin.TabularInline):
    model = Tag

# 自定义管理页面
class ContactAdmin(admin.ModelAdmin):
    #fields = ('name', 'email')
    list_display = ('name', 'age', 'email') # 增加显示页面的列
    inlines = [TagInline] #内联样式
    # 双栏目
    fieldsets = (
        ['Main',{
            'fields': ('name', 'email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS - 折叠样式
            'fields': ('age',),
        }]
    )

# 注册数据模型到admin管理器
admin.site.register(Contact, ContactAdmin)

# 注册数据模型到admin管理器
admin.site.register([Test])

#admin.site.register([Test, Tag, Contact])

