FROM python:3.10

# Install required packages
RUN apt-get update && apt-get install -y libgl1-mesa-glx \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy source code
COPY . /app
COPY .env.default /app/.env.default
COPY _docker/start.sh /usr/bin/start.sh

RUN pip install --no-cache-dir -r requirements.txt
RUN rm -rf _docker _doc docker-compose.yaml CHANGELOG.md README.md requirements.txt .gitignore .git
RUN chmod +x /usr/bin/start.sh

RUN apt-get remove -y build-essential \
        && apt-get autoremove -y \
        && apt-get clean

CMD ["/usr/bin/start.sh"]
