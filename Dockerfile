FROM python:3.9-alpine
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip --user
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]