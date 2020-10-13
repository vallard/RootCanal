FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.7
RUN  apk update && pip install --upgrade pip && pip install flask_cors 
ENV ROOT_PATH="/vol"
COPY app.py /app/main.py
