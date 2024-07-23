FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the src directory into the container
COPY ./src /app/src

# Copy the tests directory into the container
COPY ./tests /app/tests

# Install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Install Jupyter Notebook
RUN pip install jupyter

# Expose the ports for your application and Jupyter Notebook
EXPOSE 5000
EXPOSE 8888

# Start Jupyter Notebook by default
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
