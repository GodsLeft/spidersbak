#!/usr/bin/env bash
# tar -cf ../xinshou.tar ./

# scp -r data/ slave04:~/xinshou
scp -r util/ slave04:~/xinshou/
scp *.py *.sh slave04:~/xinshou/
