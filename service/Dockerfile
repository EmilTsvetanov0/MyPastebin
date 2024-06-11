FROM python:3.11.5

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY text_data.db .
COPY *.py .
COPY templates/ templates/
COPY .idea/ .idea/
COPY static/ static/

EXPOSE 1333

CMD ["python", "app.py"]

