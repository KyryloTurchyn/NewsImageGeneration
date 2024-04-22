FROM python:3.8-slim

WORKDIR /pythonProject

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118

COPY pythonProject/ .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

EXPOSE 5000

CMD ["python", "app.py"]
