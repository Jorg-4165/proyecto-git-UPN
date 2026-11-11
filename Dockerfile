FROM python:3.12-slim
WORKDIR /app
COPY notas.py test_notas.py ./
CMD ["python", "notas.py"]
