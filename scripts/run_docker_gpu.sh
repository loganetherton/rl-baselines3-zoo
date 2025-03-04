#!/bin/bash
# Launch an experiment using the docker gpu image

cmd_line="$@"

echo "Executing in the docker (gpu image):"
echo $cmd_line

docker run -it --runtime=nvidia --rm --network host --ipc=host \
  --mount src=$(pwd),target=/root/code/mle_zoo3,type=bind stablebaselines/rl-baselines3-zoo:latest\
  bash -c "cd /root/code/mle_zoo3/ && $cmd_line"
