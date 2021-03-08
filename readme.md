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
> source venv/bin/activate
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
> python3 manage.py makemigrations
> python3 manage.py migrate
> python3 manage.py runserver
> python3 manage.py createsuperuser
```

###### sqlite3 명령어 
```
> sqlite3 db.sqlite3
> .tables
> .schema fcuser
```

###### 장고 admin
* http://127.0.0.1:8000/admin

###### 참고
* https://docs.python.org/3.9/
* https://docs.djangoproject.com/en/3.1/
* https://getbootstrap.com/docs/4.6/getting-started/introduction/
* https://bootswatch.com/darkly/