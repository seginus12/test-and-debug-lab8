FROM python:3.9.18-alpine3.18
WORKDIR /usr/src/tests
COPY . .
RUN pip install pytest
CMD pytest tests.py::Tests
