from taobao.models import goods

from django.http import JsonResponse
from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage

from django.views.decorators.csrf import  csrf_exempt

#分类展示
#测试的时候我先把csrf关了
@csrf_exempt
def classify(req):
    context ={'status':200}
    #获取 post 数据
    type = req.POST.get('type','')
    page = req.POST.get('page','')
    print(page)
    context['type'] , context['page'] = type ,page
    return JsonResponse(context)
    #根据类别在数据库找到相应数据
    if type == '0':
        goods_list = goods.objects.order_by('sales_Volume').all()
    else:
        goods_list = goods.objects.all().filter(category = int(type)).order_by('sales_Volume').all()

    #数据为空直接返回json
    if goods_list == None:
        return JsonResponse({'status':10021,'message':'parameter error'})

    #分页
    paginator = Paginator(goods_list,8)
    try:
        goodss = paginator.page(int(page))
    except PageNotAnInteger:
        goodss = paginator.page(1)
    except EmptyPage:
        goodss = paginator.page(paginator.num_pages)

    #一页商品的个数，是否有前一页，是否有后一页
    context['queryNum'],context['hasPrevios'],context['hasNext'] = len(goodss),goodss.has_previous(),goodss.has_next()

    #将数据存入data[]
    data = []
    if goodss:
        for i in goodss:
            good = {}
            good['goods_id'] = i.goods_id
            good['goods_name'] = i.goods_name
            good['goods_price'] = i.goods_price
            good['goods_stock'] = i.goods_Stock
            good['sales_volume'] = i.sales_Volume
            good['goods_introduce'] = i.goods_introduce
            data.append(good)
        # 将data存进context
        context.update({'data':data})
        # 返回json
        return JsonResponse(context)
    else:
        return  JsonResponse({'status':10022,'message':'query goods isempty'})

@csrf_exempt
def test(req):
    context = {'status': 200}
    number = req.POST.get('number','')
    context['number'] = number
    question_id = req.GET.get('question_id','')
    context['question_id'] = question_id
    context['total'] = str(int(number) + int(question_id))
    if number == '1':
        # return JsonResponse({'status': 200, 'message': 'parameter error'})
        return JsonResponse(context)
    else:
        return JsonResponse({'status': 10021, 'message': 'parameter error'})
