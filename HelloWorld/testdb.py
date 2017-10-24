#!/usr/bin/env python
#coding:utf8

from django.http import HttpResponse
from TestModel.models import Test

# # 数据库操作(测试)
# def testdb(request):
#     #等同于SQL中的INSERT语句
#     test1 = Test(name='runoob5')
#     #未调用save()前，Django不会访问数据库
#     test1.save()
#     return HttpResponse("<p>数据添加成功！</p>")

# 数据库操作(获取数据)
def testdb(request):
    # 初始化
    response = ""
    response1 = ""
    
    # 通过objects这个模型管理器的all()获取所有数据行，相当于SQL中的SELECT * FROM
    alist = Test.objects.all()

    # filter相当于SQL中的WHERE,可设置条件过滤结果
    response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.get(id=1)

    # 限制返回的数据 相当于SQL中的OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]

    # 数据排序
    Test.objects.order_by("id")

    # 上面的方法可以连锁用
    Test.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in alist:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")

# # 数据库操作(更新数据)
# def testdb(request):
#     # 修改其中一个id=1的name字段,再save,相当于SQL中的UPDATE
#     test1 = Test.objects.get(id=1)
#     test1.name = 'Google'
#     test1.save()

#     # 另外一种方式
#     #Test.objects.filter(id=1).update(name='Google')

#     # 修改所有的列
#     #Test.objects.all().update(name='Google')

#     return HttpResponse("<p>修改成功</p>")

# # 数据库操作(删除数据)
# def testdb(request):
#     # 删除id=1的数据
#     test1 = Test.objects.get(id=1)
#     test1.delete()

#     # 另外一种方式
#     #Test.objects.filter(id=1).delete()

#     # 删除所有数据
#     #Test.objects.all().delete()

#     return HttpResponse("<p>删除成功</p>")