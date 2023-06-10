from django.shortcuts import render
from .models import *
from HomePage.models import TagInfo as Tag
# Create your views here.


def Get_Page(request) :
    if request.method == "GET":
        Target = Tag.objects.all()
        hot_check = ArticleInfo.objects.all().order_by('-click_num')[:5]
        str =request.GET.get('big_type',default='110')
        if str == "110" :
            All_List = ArticleInfo.objects.all().order_by('-add_time')
            Big_type = Category.objects.all()
        else :
            if str[0] == 'c':
                str = 'c/c++'
            All_List = []
            Big_type = Category.objects.all()
            List = ArticleInfo.objects.all().order_by('-add_time')
            for i in List :
                if  i.category.name == str :
                    All_List.append(i)
    return render(request , 'article.html' , locals() )

def Get_ArticleInfo(req):
    if req.method == "GET" :
        str = req.GET['id']
        Info = ArticleInfo.objects.get(id=str)
        hot_check = ArticleInfo.objects.all().order_by('-click_num')[:5]
        next_str = int(str) + 1
        up_str = int(str) - 1
        ArticleInfo.objects.filter(id=str).update(click_num=int(Info.click_num) + 1 ) # 点击数加1
        Info.click_num = int(Info.click_num) + 1
        try:
            Up_Info = ArticleInfo.objects.get(id=up_str)
            Next_Info = ArticleInfo.objects.get(id=next_str)
        except:
            Up_Info = None
            Next_Info = None

    return render(req, 'article_detail.html', locals())