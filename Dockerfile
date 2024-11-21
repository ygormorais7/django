FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

ARG UID=1000
ARG GID=1000

RUN usermod -u $UID www-data && groupmod -g $GID www-data
RUN mkdir -p /code && chown -R www-data:www-data /code
RUN chmod -R 777 /code

COPY --chown=www-data:www-data requirements.txt .
RUN pip install -r requirements.txt

COPY --chown=www-data:www-data . .
USER www-data

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
