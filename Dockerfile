From python:3.5-alpine

ENV http_proxy=http://melinet:9515
ENV https_proxy=http://melinet:9515

RUN pip install flask pytest

ADD app /opt/app/
ADD tests /opt/tests/
ADD run.py/ /opt/

EXPOSE 5000

ENTRYPOINT ["python", "/opt/run.py"]