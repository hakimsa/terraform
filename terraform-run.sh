#!/bin/bash
#docker run --rm -v $(pwd):/app -w /app terraform-container $@
docker run --rm -v $(pwd):/workspace -v /var/run/docker.sock:/var/run/docker.sock terraform-container2 $@
