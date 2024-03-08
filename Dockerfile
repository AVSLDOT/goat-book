FROM python:slim  
COPY src /src  
WORKDIR /src  
RUN pip install -r requirements.txt 
CMD python manage.py runserver 
