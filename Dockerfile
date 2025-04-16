
FROM python:3
COPY . /Blog_post
WORKDIR /Blog_post

RUN pip install - requirements.txt

CMD ["python3","manage.py","runserver","0.0.0.8000"]

