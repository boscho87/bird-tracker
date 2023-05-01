FROM python:3.10

# Install required packages
RUN apt-get update && apt-get install -y libgl1-mesa-glx \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy source code
COPY . /app
COPY _docker/entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod ug+x /usr/bin/entrypoint.sh

# Install dependencies
RUN pip install -r requirements.txt

# Run setup.py
RUN rm -rf _docker _doc docker-compose.yaml CHANGELOG.md README.md requirements.txt .gitignore .git

ARG USER_ID=1000
RUN usermod -u ${USER_ID} www-data
ENTRYPOINT [ "/usr/bin/entrypoint.sh" ]
CMD [ "python", "main.py" ]
