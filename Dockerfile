FROM python:3.9-slim

WORKDIR /app

COPY app/requirement.txt /app/requirement.txt

RUN pip install --no-cache-dir -r /app/requirement.txt

COPY app /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]