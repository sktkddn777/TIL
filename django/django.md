# Django란
- 파이썬으로 제작된 오픈소스 웹 프레임워크 입니다.  

## Django의 특징
![img](https://blog.kakaocdn.net/dn/uJODm/btq5txmspmX/q0u7UyWF7Ule8gmZcqI7Pk/img.png)

## 그 전에!!! 
MVC 모델이란. 
Model
서버가 가지고 있는 데이터베이스 작업이라고 생각하면 됩니다.  

View
브라우저 상에서 사용자에게 보여지는 페이지를 의미합니다.  

Controller
Model 에다가 일을 시키는 작업. User는 뷰를 통해 컨트롤러를 실행시켜 Model에다가 작업을 요청합니다.
View와 Model의 중간다리 역할을 하는 셈이죠.

Model       <->   Model

View         <->   Template

Controller  <->    View
1. ### MTV 패턴을 사용한다.
    * **Model**: 데이터베이스에 저장되는 데이터.  
    Django는 SQL을 몰라도 DB작업을 해주는 ORM을 제공해준다.
    
    * **Template**: 사용자에게 보여지는 부분. 

    * **View**: 뷰는 웹 요청을 받고, 전달받은 데이터들을 해당 어플리케이션의 로직으로 가공하여, 그 결과를 템플릿에 보내준다.  
       데이터를 가공하는 처리를 해야한다 싶으면 뷰에서 함수를 작성하면 된다.

    * URLconf: URL은 view와 template을 이어주는 역할을 한다. 이부분을 만들어주는 작업을 URLconf하고 한다.
2. ### ORM기능을 지원한다.
* **ORM**: Object-Relational Mapping  
    Object와 관계형 DB의 데이터를 Mapping해주는 것을 의미한다.  
    SQL이라는 언어 대신 데이터베이스를 쉽게 연결해주는 방법.  
    ```
    book_list = BookTable.query(author="Hong Jungwoo")
    ```

3. ### 자체적인 템플릿을 지원한다.
4. ### 소스코드 변경 샇항을 자동으로 반영한다.

## Django실행 방법
1. Django를 설치하고, Django 프로젝트를 시작한다.
```  
$ python -m pip install Django
$ cd djangoDirectory
$ django-admin startproject mysite
```
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
2. 프로젝트가 제대로 동작하는지 확인해 보려면 mysite 디렉토리에서 아래 코드를 실행한다.
```
$ python manage.py runserver
```

3. 앱을 만드는 방법.
```
$ python manage.py startapp my_app
```

4. 이후에 작업은 구글링 해보세요~  

[장고 nginx, uwsgi 연결하는 방법](https://github.com/sktkddn777/Django_uWSGI_NGINX)  
이 링크에 추가 작업을 해두겠습니다.