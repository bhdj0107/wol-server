FROM python:3.12.9

WORKDIR /app
RUN pip install flask_restx

COPY main.py /app/
COPY wol.py /app/

CMD ["python", "main.py"]