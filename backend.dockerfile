FROM tiangolo/uvicorn-gunicorn-fastapi:latest
WORKDIR /app/
COPY ./app /app
RUN pip install requests
EXPOSE 80
ENV PYTHONPATH=/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]