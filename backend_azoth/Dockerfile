FROM python:3.7

WORKDIR /opt/app

COPY ./requirements.txt /opt/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /opt/app

ENV PYTHONPATH /opt/app

EXPOSE 8001

CMD ["uvicorn", "AzothApp.main:app", "--host", "0.0.0.0", "--port", "8001"]