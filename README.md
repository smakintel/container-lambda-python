# python-flask-restapi
Example Project on how to develop RESTful API with Flask and Python


# Kava notes
## create virtual env in ubuntu (my dev env python version is 3.8)
cd to project directory

python3 -m venv .

source ./bin/activate

pip install -r requirements.txt

# build the image
docker build -t pythonrestapi .
# list the image
docker images


# run the container
docker run -d -p 80:80 --name pythonrestapi pythonrestapi

# Create ECR Repo if doesn't exists
sudo aws ecr create-repository --repository-name rest-api --image-scanning-configuration scanOnPush=true --image-tag-mutability IMMUTABLE --region ap-southeast-1 --profile default


docker tag pythonrestapi:latest 968262565012.dkr.ecr.ap-southeast-1.amazonaws.com/rest-api:v2


# AWS ECR login
sudo aws ecr get-login-password --region ap-southeast-1 --profile default | docker login --username AWS --password-stdin 968262565012.dkr.ecr.ap-southeast-1.amazonaws.com

docker push 968262565012.dkr.ecr.ap-southeast-1.amazonaws.com/rest-api:v2


# Example lambda test event when testing 

## for testing root path "/"

{
  "resource": "/",
  "path": "/",
  "httpMethod": "GET",
   "queryStringParameters": {
    "postcode": "12345"
  }
}

## for testing root path "/kava/test" Path
{
  "resource": "/",
  "path": "/kava/test",
  "httpMethod": "GET",
   "queryStringParameters": {
    "postcode": "12345"
  }
}



# API Gateway end point
## path=/   (as defined in app.py)
https://<################>.execute-api.ap-southeast-1.amazonaws.com/test
## path=/kava/test (as defined in app.py)
https://<################>.execute-api.ap-southeast-1.amazonaws.com/test/kava/test