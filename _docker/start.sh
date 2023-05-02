#!/bin/sh

python /app/_init.py
python /app/_app.py &
python /app/_web.py
