FROM python:3.13-slim
WORKDIR /app
COPY requirments.txt .
RUN pip install -r requirments.txt
COPY . .
EXPOSE 5000
CMD ["python", "main.py"]