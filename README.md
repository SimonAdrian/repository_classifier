## GitHub Repository Classifier

This is intended to become an end-to-end pipeline that takes as input the GitHub handle of a repository and returns as output a classification of the repository into one of multiple categories related to microservice applications.

### General Idea
In its basic form, it's a binary classifier between the categories "microservice application" and "not a microservice application".
In a more advanced version, categories should also distinguish between, e.g., repositories that contain the code for a single microservice in a larger applciation, repositories that hold configuration data, repositories that contain a collection of resources for the development of microservices, or repositories that contain frameworks for the development of microservice applications.

To reach an optimal configuration, different repository vectorizations and different classification models will be tested.
The pipeline should thus be modularized, where encoders and models can be changed easily.
First, one simple but functioning configuration should be implemented.
