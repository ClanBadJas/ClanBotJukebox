FROM python:3.10-slim
COPY ./clanbotjukebox /clanbotjukebox
WORKDIR /clanbotjukebox
RUN pip install -r requirements.txt
CMD python ./cogmanager.py
