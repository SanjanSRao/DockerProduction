# DockerProduction
# Author : Sanjan Rao
Docker container deployable to production using flask, wsgi 
Linux Docker container using python3.6 for development.
Flask has been used alongside development, wsgi and apache server for production level deployment.
Flasgger for dynamic UI Creation.

Flask_demo has script creating API's and a model created upon iris dataset for classification using RandomForest.

Build Image: docker build -t <name_of_image> .
Run Image: docker run -d -p 8000:8000 <name_of_image>
