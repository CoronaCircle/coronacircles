# start from an official image
FROM python:3.8

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/coronacircles
WORKDIR /opt/services/coronacircles

# copy our project code
COPY ./ /opt/services/coronacircles/

# install our dependencies
RUN pip install pipenv
RUN pipenv lock
RUN pipenv install --system

# expose the port 8000
EXPOSE 8000