FROM python:3.6
WORKDIR /deploy/
COPY ./requirements.txt /deploy/
COPY ./webapp_predict_price /deploy/webapp_predict_price
RUN pip install -r ./requirements.txt
CMD ["python", "webapp_predict_price/__init__.py"]~