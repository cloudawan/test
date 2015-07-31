FROM    centos:centos6

# To download pip
RUN     rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
# Install pip
RUN     yum install -y python-pip
# Install Flask for REST API
RUN     pip install Flask


# Bundle app source
COPY . /src

EXPOSE  8080
CMD ["python", "/src/flask/rest_api.py"]
