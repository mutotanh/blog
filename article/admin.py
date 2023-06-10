from django.contrib import admin

# Register your models here.
from article.models import *

# Register your models here.
admin.site.register(ArticleInfo)
admin.site.register(TagInfo)
admin.site.register(Category)