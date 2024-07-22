FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the project code into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Install Jupyter Notebook
RUN pip install jupyter

# Expose the ports for your application and Jupyter Notebook
EXPOSE 5000
EXPOSE 8888

# Start Jupyter Notebook by default
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
