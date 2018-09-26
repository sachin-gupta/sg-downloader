#!/bin/bash

#Build Docker Image Iff ${DOCKER_BUILDIMAGE} == TRUE, Commit iff ${DOCKER_COMMITIMAGE=TRUE}
set -ev

if [ "${DOCKER_BUILDIMAGE}" = "true" ]; then
    # Now build the docker image from Dockerfile with ${DOCKER_APPNAME}
    echo "~~~ Building Docker Image ~~~"
    echo "${DOCKER_USERNAME}/${DOCKER_APPNAME}:${DOCKER_TAG}"
    docker build -t "${DOCKER_USERNAME}/${DOCKER_APPNAME}:${DOCKER_TAG}" -t "${DOCKER_USERNAME}/${DOCKER_APPNAME}:latest" .
    
    # Check the present images in the our system [${DOCKER_APPNAME} Should Appear]
    docker images
    docker history "${DOCKER_USERNAME}/${DOCKER_APPNAME}:${DOCKER_TAG}"
    
    # Run our application inside docker image ${DOCKER_APPNAME} using docker run
    docker run ${DOCKER_USERNAME}/${DOCKER_APPNAME}:${DOCKER_TAG}
    
    # Check that our application inside docker image ${DOCKER_APPNAME} created a container
    docker ps --all
    
    # Save compiled docker image with application as tar file for later use
    docker save -o ${DOCKER_APPNAME}_${DOCKER_TAG}.tar ${DOCKER_USERNAME}/${DOCKER_APPNAME}:${DOCKER_TAG}
    
    if [ "${DOCKER_COMMITIMAGE}" = "true" ]; then
        echo "~~~ Pushing Image To DockerHub ~~~"
        # Login to dockerhub and push image as full name and tag
        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
        ##- docker tag ${DOCKER_APPNAME} ${DOCKER_USERNAME}/${DOCKER_APPNAME}:${DOCKER_TAG}
        docker push ${DOCKER_USERNAME}/${DOCKER_APPNAME}:${DOCKER_TAG}
    fi
fi
