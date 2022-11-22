FROM python:3.9

WORKDIR ./code

RUN pip install requests streamlit

COPY ./ /code

CMD ["streamlit", "run", "app.py"]