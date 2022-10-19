FROM python:3

ADD bot_main.py /

RUN pip install discord-py
RUN pip install youtube-dl
RUN pip install pafy
RUN pip install cryptocode
RUN pip install PyNaCl

CMD [ "python", "./bot_main.py" ]
