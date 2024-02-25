FROM python:3.7-slim
COPY dash-container .
RUN pip install -r requirements.txt
CMD ["gunicorn", "-b", "0.0.0.0:8080", "online-shop:server"]