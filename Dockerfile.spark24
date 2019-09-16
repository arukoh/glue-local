FROM python:3.7-alpine

ENV SPARK_HOME /spark
ENV SPARK_VERSION 2.4.4
ENV HADOOP_VERSION 2.7

# Install OpenJDK
RUN apk add --update \
    bash \
    zip \
    git \
    openjdk8 \
    maven \
  && rm -rf /var/cache/apk/*

# Install Spark
#RUN wget -q http://apache.mirror.iphh.net/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
RUN wget -q https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
  && tar xzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
  && mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} ${SPARK_HOME} \
  && rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz

# Install AWS Glue Python Library
RUN pip install pyspark \
  && rm -rf ~/.cache/pip
RUN git clone https://github.com/awslabs/aws-glue-libs.git /aws-glue-libs \
  && cd /aws-glue-libs \
  && bash ./bin/glue-setup.sh

ENV PATH /aws-glue-libs/bin:$PATH
ENV PYSPARK_GATEWAY_SECRET dummy
ENV AWS_ACCESS_KEY_ID dummy
ENV AWS_SECRET_ACCESS_KEY dummy
ENV AWS_REGION us-east-1
ENV AWS_DEFAULT_REGION us-east-1
