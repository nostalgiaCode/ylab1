FROM python:3.10-slim
WORKDIR /appplication
COPY . /appplication
RUN pip install --upgrade pip --user
RUN pip install -r requirements.txt
EXPOSE 80
CMD ["uvicorn", "run:server", "--host", "0.0.0.0", "--port", "80"]
