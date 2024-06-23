FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install base system dependencies
RUN apt update -y
RUN apt install -y dos2unix

# Install third-party dependencies
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /opt/bin/
RUN chmod +x /opt/bin/wait-for-it.sh

# Install python dependencies
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Move base project files
COPY start.sh /
RUN chmod +x /start.sh
RUN dos2unix /start.sh

CMD /opt/bin/wait-for-it.sh --timeout=20 $DATABASE_HOST:$DATABASE_PORT -- /start.sh