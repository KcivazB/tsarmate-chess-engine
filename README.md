# Chess Engine Project

## Overview
This project involves creating a scalable chess engine using Python and Go, adhering to Test-Driven Development (TDD) principles, and deploying it with Docker and Kubernetes.

## Project Structure

### Python Implementation
- **Directory**: `chess_engine_python/`
  - `src/`: Source code for the Python implementation.
  - `tests/`: Unit and integration tests.
  - `requirements.txt`: Python dependencies.

### Go Implementation
- **Directory**: `chess_engine_go/`
  - `src/`: Source code for the Go implementation.
  - `tests/`: Unit and integration tests.
  - `go.mod`: Go module dependencies.

### Docker and Kubernetes
- **Directory**: `chess_engine/`
  - `python/`: Dockerfile for Python component.
  - `go/`: Dockerfile for Go component.
  - `docker-compose.yml`: Local development and testing setup.
  <!-- - `k8s/`: Kubernetes manifests for deployment. -->
  - `README.md`: Project documentation.

## Phases and Milestones

### Phase 1: Python Implementation
- **Week 1**: Basic board setup and move generation.
- **Week 2**: Evaluation functions, simple AI, and advanced TDD.

### Phase 2: Transition to Go
- **Week 3**: Learn Go, set up project, and initial Go implementation.
- **Week 3-4**: Performance optimization and integration with Python.

### Phase 3: Containerization and Kubernetes
- **Week 4**: Dockerize the application.
- **Week 4-5**: Deploy on Kubernetes, implement scaling, monitoring, and CI/CD.

## Setup Instructions

### Prerequisites
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
<!-- - **Kubernetes**: [Install Minikube](https://minikube.sigs.k8s.io/docs/start/) -->

### Docker
1. Navigate to `tsarmate_chess_engine/`.
2. Build Docker images: `docker-compose build`
3. Run Docker containers: `docker-compose up`

<!-- 
### Kubernetes
1. Start a local Kubernetes cluster: `minikube start`
2. Deploy services: `kubectl apply -f k8s/`
3. Verify deployment: `kubectl get pods` -->

## Contribution
Feel free to submit issues or pull requests. Ensure to follow the project's coding standards and include appropriate tests.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For questions or feedback, open an issue or contact the maintainer.

---

**Happy coding!** 🚀
