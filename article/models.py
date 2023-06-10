from django.db import models
from datetime import datetime
# Create your models here.
import random
from DjangoUeditor.models import UEditorField

class Category(models.Model):
	name = models.CharField(max_length=20, verbose_name='类别名')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
	is_tab = models.BooleanField(default=True, verbose_name='是否导航')
	title = models.CharField(max_length=50, verbose_name='类别标题', null=True, blank=True)
	path_name = models.CharField(max_length=15, verbose_name='路径别名', null=True, blank=True)
	objects = models.Manager()
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = '类别表'
		verbose_name_plural = verbose_name

import time

m_y=(time.strftime("%Y"))
m_m=(time.strftime("%m"))



class TagInfo(models.Model):
	name = models.CharField(max_length=20, verbose_name='标签名')
	add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
	category = models.ForeignKey(Category, verbose_name='所属类别', null=True, blank=True ,on_delete=models.DO_NOTHING)
	objects = models.Manager()
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = '标签表'
		verbose_name_plural = verbose_name

class ArticleInfo(models.Model):
	title = models.CharField(max_length=50, verbose_name='标题')
	desc = models.TextField(max_length=80, verbose_name='简介')
	content = UEditorField('内容', width=800, height=500,
                    toolbars="full", imagePath="upimg/", filePath="upfile/",
                    upload_settings={"imageMaxSize": 10240000000},
                    settings={}, command=None, blank=True
                    )
	click_num = models.IntegerField(default=0, verbose_name='浏览数')
	cont_num = models.IntegerField(default=0, verbose_name='评论数')
	love_num = models.IntegerField(default=0, verbose_name='点赞数')
	image = models.ImageField(upload_to='upfile/', verbose_name='封面', max_length=200,default='None', null=True, blank=True)
	add_time = models.DateTimeField(default=datetime.now, verbose_name='发表时间')
	is_recommend = models.BooleanField(default=False, verbose_name='首页推荐')
	category = models.ForeignKey(Category, verbose_name='所属类别', null=True, blank=True ,on_delete=models.DO_NOTHING)
	taginfo = models.ForeignKey(TagInfo, verbose_name='所属标签',null=True,blank=True,on_delete=models.DO_NOTHING)
	objects = models.Manager()
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = '文章表'
		verbose_name_plural = verbose_name

