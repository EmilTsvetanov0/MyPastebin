FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

COPY *.py /app/
COPY tokenizer.pkl /app/

COPY requirements.txt /app/

WORKDIR /app/

#RUN pip install torch torchvision -f https://download.pytorch.org/whl/torch_stable.html --no-cache-dir
RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "80"]
