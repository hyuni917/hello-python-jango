###### 가상환경 설정을 위한 패키지 설치
```
> pip3 install virtualenv
```

###### 가상환경 생성
```
> virtualenv venv
```

###### 가상환경 활성화
```
> (mac) source venv/bin/activate
> (win) call venv/scripts/activate
```

###### 장고 설치
```
> pip3 install django
```

###### 장고 프로젝트 생성
```
> django-admin startproject community
> cd community
```

###### 장고 앱 생성
```
> django-admin startapp board
> cd board
> mkdir templates
> cd ..
> django-admin startapp user
> cd user
> mkdir templates
> cd ..
```

###### python3 manage.py cmd   
```
> (mac) python3 manage.py makemigrations
> (win) manage.py makemigrations

> (mac) python3 manage.py migrate
> (win) manage.py migrate

> (mac) python3 manage.py runserver
> (win) manage.py runserver

> (mac) python3 manage.py createsuperuser
> (win) manage.py createsuperuser
```

###### sqlite3 명령어 
```
> sqlite3 db.sqlite3
> .tables
> .schema user
```

###### 장고 admin
* http://127.0.0.1:8000/admin

###### 참고
* https://docs.python.org/3.9/
* https://docs.djangoproject.com/en/3.1/
* https://www.sqlite.org/index.html
* https://getbootstrap.com/docs/4.6/getting-started/introduction/
* https://bootswatch.com/darkly/