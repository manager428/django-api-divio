# <WARNING>
# Everything within sections like <TAG> is generated and can
# be automatically replaced on deployment. You can disable
# this functionality by simply removing the wrapping tags.
# </WARNING>

FROM python:3.11
ENV PYTHONUNBUFFERED 1
COPY requirements.* /app/

RUN pip install -r requirements.txt
# </PYTHON>
# test
# <SOURCE>
COPY . /app
# </SOURCE>

# <GULP>
# </GULP>

# <STATIC>
# RUN DJANGO_MODE=build python manage.py collectstatic --noinput
# </STATIC>
