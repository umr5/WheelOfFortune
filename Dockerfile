FROM python:latest

ADD server.py /server/
ADD word_game.py /server/
ADD phrases.txt /server/

WORKDIR /server/

CMD [ "python", "./server.py"]

