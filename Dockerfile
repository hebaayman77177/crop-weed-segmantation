FROM python:3.6-slim
WORKDIR /usr/src/app
COPY . .
RUN pip3 install pipenv
RUN pipenv install
EXPOSE 5000
CMD ["pipenv", "run", "python", "api.py"]
