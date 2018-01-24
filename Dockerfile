FROM python AS core_telegram
COPY requirements.txt /project/requirements.txt
WORKDIR /project
RUN pip install -r requirements.txt
EXPOSE 80