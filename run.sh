#!/bin/bash

python3 run.py
git add .
git commit -m "auto commit rnd `date '+%Y%m%d %H:%M:%S'`"
git push origin master
