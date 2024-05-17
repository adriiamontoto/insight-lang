FROM python:3.11

WORKDIR /home/backend

COPY /.env ./.env
COPY ./backend/ ./

RUN pip install --no-cache-dir --disable-pip-version-check --upgrade -r requirements.txt
RUN rm -rf requirements.txt requirements_dev.txt test/

CMD ["python", "main.py"]
