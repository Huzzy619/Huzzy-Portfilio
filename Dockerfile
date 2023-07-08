FROM python:3.10-alpine3.18
# FROM python:3.9-slim-buster
# FROM python:3.10-slim



WORKDIR /app


ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV SECRET_KEY=${SECRET_KEY}
 

ENV TREBLLE_API_KEY=${TREBLLE_API_KEY}
ENV TREBLLE_PROJECT_ID=${TREBLLE_PROJECT_ID}
ENV OPENAI_API_KEY=${OPENAI_API_KEY}
ENV DEBUG=${DEBUG}
ENV DATABASE_URL=${DATABASE_URL}
ENV STRIPE_SECRET_KEY=${STRIPE_SECRET_KEY}
# ENV DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}


COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt  


COPY . .


RUN python3  manage.py collectstatic --no-input

RUN python3 manage.py migrate

EXPOSE 8001

CMD ["gunicorn", "--bind", "0.0.0.0:8001", "MyWeb.wsgi"]
# CMD [ "python3", "manage.py", "runserver","0.0.0.0:8000" ]



