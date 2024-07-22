# Dockerfile for Go component

# Use the official Go image from the Docker Hub
FROM golang:1.22-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the Go module files
COPY go.mod go.sum ./

# Download Go module dependencies
RUN go mod download

# Copy the source code into the container
COPY src/ ./src

# Build the Go application
RUN go build -o main ./src

# Set the entry point for the container
CMD ["./main"]
