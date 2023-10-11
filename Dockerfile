FROM python

WORKDIR /app

COPY . .

RUN sudo apt-get -y install python3-pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT python app.py
