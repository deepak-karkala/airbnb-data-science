FROM python:3.6
WORKDIR /deploy/
COPY ./requirements.txt /deploy/
COPY ./instance /deploy/instance
COPY ./webapp_alternate_search /deploy/webapp_alternate_search
RUN pip install -r ./requirements.txt
CMD ["python", "webapp_alternate_search/__init__.py"]~
