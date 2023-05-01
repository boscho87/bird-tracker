FROM python:3.10

# Install required packages
RUN apt-get update && apt-get install -y libgl1-mesa-glx \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy source code
COPY _docker /app
COPY entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod ug+x /usr/bin/entrypoint.sh

# Install dependencies
RUN pip install -r requirements.txt

# Run setup.py
RUN python setup.py install

ENTRYPOINT [ "entrypoint.sh" ]
CMD [ "python", "main.py" ]
