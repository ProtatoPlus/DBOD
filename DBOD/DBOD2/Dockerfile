FROM python:3

ADD createmain.py /
ADD main.py /

RUN pip3 install cherrypy
RUN pip3 install docker

CMD [ "python3", "./main.py" ]
