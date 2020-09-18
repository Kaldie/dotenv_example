FROM python:3

COPY . /src
RUN pip install -r /src/require.txt

ARG KEY
ENV KEY=$KEY

ARG PASSWORD
ENV PASSWORD=$PASSWORD


ENTRYPOINT [ "python", "/src/script.py" ]