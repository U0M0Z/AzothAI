FROM python:3.7

WORKDIR /opt/app

COPY ./requirements.txt /opt/app/requirements.txt

RUN pip install -r requirements.txt

COPY . /opt/app

ENV PYTHONPATH /opt/app

EXPOSE 8501

CMD ["streamlit", "run", "main_gui.py", "--server.port=8501", "--server.address=0.0.0.0"]