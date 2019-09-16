FROM python:alpine

RUN pip install awscli \
  && rm -rf ~/.cache/pip

ENV AWS_ACCESS_KEY_ID 'dummy'
ENV AWS_SECRET_ACCESS_KEY 'dummy'
ENV AWS_REGION 'ap-northeast-1'
ENV AWS_DEFAULT_REGION 'ap-northeast-1'
