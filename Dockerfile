FROM python:3.12.9

WORKDIR /app
COPY main.py /app/
COPY wol.py /app/

RUN pip install flask_restx

CMD ["python", "main.py"]