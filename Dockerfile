FROM python:3.7-alpine3.12

ADD requirements.txt /
ADD task.py /

RUN mkdir ./data
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

CMD ["python", "-u", "./task.py"]