FROM python:3.10

# Install required packages
RUN apt-get update && apt-get install -y libgl1-mesa-glx \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy source code
COPY . /app
COPY .env.default /app/.env.default
# Install dependencies
RUN pip install -r requirements.txt
RUN rm -rf _docker _doc docker-compose.yaml CHANGELOG.md README.md requirements.txt .gitignore .git
ARG DB_FILE_PATH=/app/data/db.sqlite
RUN python setup.py install
CMD python /app/src/web/page.py & python /app/main.py
