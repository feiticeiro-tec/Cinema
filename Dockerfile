FROM python:3.10
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT flask run --host=0.0.0.0
