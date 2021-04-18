1.项目虚拟环境 flask_demo


2.ps -ef|grep uwsgi |grep -v grep|awk '{print $2}'|xargs kill -9


3. pip install Flask-Script
   pip install flask-migrate

3. python main.py runserver --host 192.168.249.128 --port 7777
3. python main.py runserver -h 192.168.249.128 -p 7777

