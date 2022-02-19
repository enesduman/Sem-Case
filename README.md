# Cars.com

Yapılması gerekenler:

## Projeyi Locale Çekme

```
cd /Desktop

Bilgisayarda git kurulu değilse terminal ekranından ' sudo apt install git '

git clone <project_url>

```

## Virtual Environment Kurulumu

```
sudo pip install virtualenv

cd /Desktop/Sem-Case

virtualenv .venv/
```

## Proje Yapılandırması

```
cd Sem-Case

source .venv/bin/activate

pip install -r requirements.txt (proje gereklilikleri kurulur.)

export FLASK_APP=main

flask run

```

### Tüm adımları tamamladıktan sonra internet tarayıcısından local portunda proje çalışır durumda olucaktır.

```
http://127.0.0.1:5000/cars/list Filtresiz 50 araç getirir.

http://127.0.0.1:5000/cars/list?extcolor=black siyah renkli araçları getirir.

http://127.0.0.1:5000/cars/list?brand=BMW&extcolor=black siyah renkli BMW araçları getirir.

http://127.0.0.1:5000/cars/list?trans=automatic&brand=Ford&year=2018 Otomatik vites türünde 2018 model Ford marka araçları getirir.

Parametreler dinamik olup doğru parametre girildiği sürece araçlar listelenecektir.

```
