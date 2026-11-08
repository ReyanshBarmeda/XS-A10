# XS-A10

<p align="center">
  <strong>An Experimental GPU and Compute Accelerator Architecture</strong>
</p>

<p align="center">
  Exploring hardware architecture, instruction execution, software tooling, and verification.
</p>

<p align="center">
  <a href="docs/installation.md">Installation</a> |
  <a href="docs/tech_details.md">Technical Documentation</a> |
  <a href="docs/verification.md">Verification</a> |
  <a href="examples/README.md">Examples</a>
</p>

---

## Overview

**XS-A10** is an experimental GPU and compute-accelerator development project focused on exploring processor architecture, hardware implementation, and supporting software infrastructure.

The project brings together hardware description, instruction-level tooling, code generation, simulation, and verification within a unified development environment.

XS-A10 aims to provide a practical foundation for experimenting with compute hardware, understanding architectural design decisions, and developing the tools required to support an accelerator platform.

The project is under active development. Hardware capabilities, performance characteristics, and implementation status should be considered experimental until verified.

## Core Components

### Hardware Architecture
Hardware implementation and supporting design components organized for modular development and experimentation.

### Software Toolchain
Python-based assembler, generation utilities, and supporting tools for working with the project's instruction and execution workflows.

### Compute Workloads
C and C++ examples demonstrating arithmetic operations, matrix multiplication, and data-transfer-related functionality.

### Simulation and Verification
Development workflows involving behavioral simulation, Verilator, gate-level simulation, and automated testing.

### Timing and Analysis
Utilities and documentation for investigating hardware timing characteristics and implementation behavior.

## Architecture and Development Workflow

The project is organized into multiple development areas:

| Directory | Description |
|---|---|
| `src/` | Core implementation sources |
| `prot/` | Hardware-related project sources |
| `XS A10/` | Python utilities, assembler, and generation tools |
| `examples/` | Example programs and compute workloads |
| `test/` | Testing and verification resources |
| `docs/` | Technical documentation and development guides |
| `third_party/` | External dependencies |
| `cicd/` | Build and verification scripts |
| `cmake/` | Build configuration and integration helpers |
| `tech/` | Technical resources |

## Technology Stack

The repository currently includes tools and technologies from the following areas:

| Technology | Purpose |
|---|---|
| SystemVerilog | Hardware description and verification |
| Python | Assembler, generation, and timing utilities |
| C/C++ | Example workloads and supporting software |
| CMake | Build configuration |
| LLVM/Clang | Compiler integration |
| Yosys | Hardware synthesis |
| Verilator | Hardware simulation and verification |
| Git | Version control |

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ReyanshBarmeda/XS-A10.git
cd XS-A10
```

### 2. Environment Setup

Review the installation documentation for required dependencies and configuration instructions.

[Installation Guide](docs/installation.md)

### 3. Explore the Examples

The `examples/` directory contains example workloads and development resources.

Start with:

[Examples Documentation](examples/README.md)

### 4. Explore Verification

The repository includes testing and verification resources for evaluating implementation behavior.

Refer to:

- [Verification Guide](docs/verification.md)
- [Verification Guidelines](docs/verification_guidelines.md)

## Documentation

| Document | Description |
|---|---|
| [Installation](docs/installation.md) | Environment setup and dependencies |
| [Technical Details](docs/tech_details.md) | Architecture and implementation details |
| [Planning](docs/planning.md) | Development planning |
| [Assembler](docs/assembler.md) | Assembler documentation |
| [States](docs/states.md) | Project state information |
| [Verification](docs/verification.md) | Verification workflows |
| [Coding Guidelines](docs/coding_guidelines.md) | Development conventions |
| [Examples](examples/README.md) | Example programs |

## Development Roadmap

Development priorities include:

- Refining hardware architecture and modularity.
- Expanding compute functionality.
- Improving assembler and software tooling.
- Strengthening behavioral and gate-level verification.
- Improving timing analysis and hardware optimization.
- Expanding documentation and example workloads.

The roadmap will evolve alongside implementation progress and verification results.

## Contributing

Contributions, technical discussions, suggestions, and improvements are welcome.

To contribute:

1. Review the existing architecture and documentation.
2. Identify a specific improvement or issue.
3. Implement changes following the project's development conventions.
4. Run relevant tests and verification workflows.
5. Document changes and provide verification details when submitting a pull request.

All contributions should distinguish verified functionality from experimental or incomplete implementation.

## Project Status

**Status: Experimental / Under Active Development**

XS-A10 is an ongoing hardware and software development project.

Not all components or workflows should be considered complete or production-ready. Physical hardware availability, compatibility, and performance should not be assumed without supporting validation.

## Project Goals

The long-term objective is to develop a well-documented and verifiable compute-accelerator architecture supported by a practical software toolchain and development ecosystem.

The project emphasizes:

- Architectural experimentation.
- Hardware and software integration.
- Reproducible verification.
- Maintainable implementation.
- Transparent technical documentation.

## License

Refer to the repository's license file for licensing terms and usage permissions.

---

<p align="center">
  <strong>XS-A10</strong><br>
  Engineering Compute Architecture Through Experimentation and Verification.
</p>
