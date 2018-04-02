FROM python AS core_telegram
COPY requirements.txt /project/requirements.txt
WORKDIR /project
RUN pip install -r requirements.txt
# ENTRYPOINT ["/bin/bash", "-c", "python local.py"] 
EXPOSE 80
