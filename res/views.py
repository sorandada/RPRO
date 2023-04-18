import requests

from django.shortcuts import render, get_object_or_404

def index(request):
    HotpepperApiKey = "あなたのホットペッパーグルメサーチAPI"

    #index.htmlのjavascriptで取得された、緯度・経度を受け取る
    if request.method == 'GET' and 'lat' in request.GET and 'lon' in request.GET:
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        range = request.GET.get('range', '3') # デフォルト値は3
        range_m = "1km"# デフォルト値は1km

        # rangeの値によって、APIに渡す範囲を変える
        if range == '1':
            range = 1
            range_m = "300m"
            range = request.GET.get('range', '1') 
        elif range == '2':
            range = 2
            range_m = "500m"
            range = request.GET.get('range', '2') 
        elif range == '3':
            range = 3
            range_m = "1km"
            range = request.GET.get('range', '3') 
        elif range == '4':
            range = 4
            range_m = "2km"
            range = request.GET.get('range', '4') 
        elif range == '5':
            range = 5
            range_m = "3km"
            range = request.GET.get('range', '5') 
        
        hotpepperURL = 'https://webservice.recruit.co.jp/hotpepper/gourmet/v1/'
        params = {
            'key': HotpepperApiKey,
            'lat': lat,
            'lng': lon,
            'range': range,
            'count':100,
            'format': 'json',
        }

        response = requests.get(hotpepperURL, params=params)

        if response.status_code == 200:
            data = response.json()['results']['shop']
            shop_num = response.json()['results']
            return render(request, 'App_Folder_HTML/index.html', {'data': data, 'range': range, "shop_num":shop_num, "range_m":range_m})
        else:
            return render(request, 'App_Folder_HTML/index.html', {'data': [], 'range': range})
    else:
        return render(request, 'App_Folder_HTML/index.html', {'data': [], 'range': '3'})



def shop_detail(request, shop_id):

    GoogleMapApiKey="あなたのGoogleMapAPI"
    HotpepperApiKey = "あなたのホットペッパーグルメサーチAPI"

    url = 'https://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

    d_params = {
        'key': HotpepperApiKey,
        'id': shop_id,
        'format': 'json',
    }
    response = requests.get(url, params=d_params)
    Ddata = response.json()['results']['shop']

    return render(request, 'App_Folder_HTML/detail.html', {'Ddata': Ddata, 'GoogleMapApiKey': GoogleMapApiKey})
