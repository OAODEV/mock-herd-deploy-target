FROM us.gcr.io/lexical-cider-93918/basebottle:_build.0273acb
MAINTAINER jesse.miller@adops.com

# set up for configurability
RUN mkdir /secret

# create a working directory
RUN mkdir /app
WORKDIR /app

# add the api
ADD service /app/service

CMD python3 -u service
