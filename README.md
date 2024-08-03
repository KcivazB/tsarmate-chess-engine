# TsarMate

## Overview
TsarMate is a Go-based chess engine designed for high performance and advanced chess analysis. It aims to implement various sophisticated techniques and algorithms to achieve optimal gameplay.

## Planned Features
- **Bitboard Representation**: Efficient board representation using bitboards.
- **Precalculated Attack Tables**: Fast access to attack patterns.
- **Magic Bitboards**: Efficient sliding piece attacks using magic bitboards.
- **Copy/Make Move Approach**: Efficient move generation and application.
- **Negamax with Alpha-Beta Pruning**: Advanced search algorithm for decision making.
- **Move Ordering**: Techniques such as Principal Variation (PV), Killer Moves, and History Moves.
- **Transposition Tables**: Efficient state caching to avoid redundant calculations.
- **Comprehensive Evaluation**: Evaluation based on material, positions, pieces, mobility, and king safety.
- **UCI Protocol**: Full compliance with the Universal Chess Interface for compatibility with chess GUIs.

## Project Structure
- **src/**: Source code for the chess engine.
- **tests/**: Unit and integration tests.
- **go.mod**: Go module dependencies.
- **README.md**: Project documentation.

## Getting Started

### Prerequisites
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)

### Build and Run
1. Clone the repository:
   ```sh
   git clone https://github.com/KcivazB/tsarmate.git
   cd tsarmate
