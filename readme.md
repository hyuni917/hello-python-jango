###### 가상환경 설정을 위한 패키지 설치
```
> pip3 install virtualenv
```

###### 가상환경 생성
```
> virtualenv --python=python3.9 venv
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

###### 장고 rest framework 설치
```
> pip3 install djangorestframework
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

> (mac) python3 manage.py collectstatic
> (win) manage.py collectstatic
```

###### uwsgi(Application Container)
```
> pip3 install uwsgi
> uwsgi --http :8000 --home /home/venv/ --chdir /home/shopping/ --module shopping.wsgi
```

###### flake8 (파이썬 코드 스타일을 검사해주는 도구)
```
> pip3 install flake8
> flake8 hello.py
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
* https://summernote.org/
* https://bootswatch.com/darkly/
* https://docs.microsoft.com/ko-kr/azure/architecture/best-practices/api-design
* https://www.django-rest-framework.org/
* https://jquery.com/

###### PEP
* PEP Python Enhance Proposal (파이썬 개선 제안서) https://www.python.org/dev/peps/pep-0001/
* Style Guide for Python Code (파이썬 코드를 위한 가이드 라인) https://www.python.org/dev/peps/pep-0008/
* The zen of Python https://www.python.org/dev/peps/pep-0020/

