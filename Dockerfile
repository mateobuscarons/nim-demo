FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
ENV API_KEY="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"
EXPOSE 8012 8080
CMD ["python", "app.py"]
