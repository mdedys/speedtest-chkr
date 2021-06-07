#!/bin/bash

rm -rf ./data
mkdir ./data

docker build . -t speedtest-chkr:latest
docker run -d --rm -v $(pwd)/data:/data --name speedtest speedtest-chkr:latest