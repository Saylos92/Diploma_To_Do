FROM python:3.13

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x start.sh

CMD ["/bin/bash","-c","./start.sh"]