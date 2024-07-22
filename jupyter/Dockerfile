# Dockerfile for Jupyter Notebook with Python support

FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install Jupyter Notebook
RUN pip install jupyter

# Copy the project code and notebooks
COPY . /app

# Expose port 8888 for Jupyter
EXPOSE 8888

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
