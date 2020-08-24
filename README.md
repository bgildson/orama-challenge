# ORAMA-CHALLENGE

[![Test Status](https://github.com/bgildson/orama-challenge/workflows/Test%20and%20Report%20Coverage/badge.svg)](https://github.com/bgildson/orama-challenge/actions?workflow=test)
[![Coverage Status](https://coveralls.io/repos/github/bgildson/orama-challenge/badge.svg?branch=master)](https://coveralls.io/github/bgildson/orama-challenge?branch=master)

This project contains the solution to the [Órama Challenge](./challenge). The solution contains a rest api with the route **/api/freelancers/compute-skills** that can receive a **POST** request with the payload to compute.

**To follow the steps bellow, you should have [Docker](https://docs.docker.com/get-docker/) installed.**

## Running the app

Build the docker image
```sh
docker build -t bgildson/orama-challenge .
```

And run the container
```sh
docker run --rm -it -p 5000:5000 bgildson/orama-challenge
```

After the steps above, the api will be running at **http://localhost:5000**.

Extra: This [file](./orama-challenge.collection.json) contains a **Postman Collection** to simulate the challenge example provided.
