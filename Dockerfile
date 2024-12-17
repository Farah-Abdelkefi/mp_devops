
# FROM vulnerables/web-dvwa


# CMD ["sh"]

FROM python:3.9-slim

WORKDIR /app
COPY . /app
RUN pip install pytest
CMD ["python", "username_generator.py"]
