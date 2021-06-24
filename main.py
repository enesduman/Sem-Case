from os import EX_CANTCREAT
from flask import Flask,request
from bs4 import BeautifulSoup
from flask.json import jsonify
import requests

app = Flask(__name__)




@app.route("/cars/list", methods=['GET'])
@app.route("/cars/list/<string:id>", methods=['GET'])
def car_list(id=None):
    req = request.args.get
    if id==None:
        id = '50'
    try:
        if req('trans') and req('brand') and req('year') and req('extcolor'):
            url = "https://www.cars.com/shopping/results/?exterior_color_slugs[]="+req('extcolor')+"&makes[]="+req('brand').lower()+"&page_size="+id+"&transmission_slugs[]="+req('trans')+"&year_max="+req('year')+"&year_min="+req('year')
        elif req('extcolor') and req('brand'):
            url = "https://www.cars.com/shopping/results/?exterior_color_slugs[]="+req('extcolor')+"&makes[]="+req('brand').lower()+"&page_size="+id
        elif req('extcolor'):
            url = "https://www.cars.com/shopping/results/?exterior_color_slugs[]="+req('extcolor')+"&page_size="+id
        elif req('trans') and req('brand') and req('year'):
            url = "https://www.cars.com/shopping/results/?makes[]="+req('brand').lower()+"&page_size="+id+"&transmission_slugs[]="+req('trans')+"&year_max="+req('year')+"&year_min="+req('year')
        elif req('brand'):
            url = "https://www.cars.com/shopping/results/?makes[]="+req('brand').lower()+"&page_size="+id
        else:
            url = "https://www.cars.com/shopping/results/?page=1&page_size="+id
    except Exception as e:
        url = "https://www.cars.com/shopping/results/?page=1&page_size="+id
    cx = {
        'advert_title':'',
        'car_price':'',
        'car_photo_url':'',
        'car_brand':'',
        'car_model_year':'',
        'car_color':'',
        'gear_type':''
    }
    all_cars= []

    response = requests.get(url)
    source= BeautifulSoup(response.content,"html.parser") 
    cars = source.find_all("div",{"class":"vehicle-card"})
    for car in cars:
        car_id = car.get('id')
        detail_url = "https://www.cars.com/vehicledetail/"+car_id
        new_response = requests.get(detail_url)
        new_source = BeautifulSoup(new_response.content,"html.parser")
        advert_title = new_source.find_all("li",{"aria-current":"page"})
        car_price = new_source.find_all("span",{"class":"primary-price"})
        car_photo_url = new_source.find_all("img",{"class":"row-pic selected"})
        car_brand = new_source.find_all("h1",{"class":"listing-title"})
        car_model_year = new_source.find_all("h1",{"class":"listing-title"})
        car_color_details = new_source.find('dt',text='Exterior color')
        car_gear_type_details = new_source.find('dt',text='Transmission')
        try:
            cx = {
            'advert_title':advert_title[0].text,
            'car_price':car_price[0].text,
            'car_brand':car_brand[0].text[4:],
            'car_model_year':car_model_year[0].text[0:4],
            'car_photo_url':car_photo_url[0]['src'],
            'car_color':car_color_details.find_next_sibling('dd').text,
            'gear_type':car_gear_type_details.find_next_sibling('dd').text
            }
        except:
             cx = {
            'advert_title':'Hata',
            'car_price':'Hata',
            'car_brand':'Hata',
            'car_model_year':'Hata',
            'car_photo_url':'Hata',
            'car_color':'Hata',
            'gear_type':'Hata'
            }

        all_cars.append(cx)
    return jsonify(all_cars)