#dockerfile for launching a flask (wordpress?) app based on a genome string

#master application that spawns and kills off new instances?

#SEO degrees of freedom

# start with a base image
FROM ubuntu:14.10

# install dependencies
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install flask docker-py

# update working directories
ADD . /app

CMD python3 app/organism.py