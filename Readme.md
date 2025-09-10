# Semantic Holder (SH) - Algebraic Extraction for Legal Opposability

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Research](https://img.shields.io/badge/status-research--implementation-orange)

A reference implementation of the **Semantic Holder (SH)** primitive, the opposability layer of the broader **CASH framework** (Chaotic Affine Secure Hash). SH enables cryptographically verifiable legal opposability through algebraic extraction from polynomial iteration traces, providing mathematically proven guarantees with minimum opposability bounds.

> **Research Implementation Notice**: This project is a theoretical construct and reference implementation intended for research validation. It is not yet audited or ready for production use.

## Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Theoretical Foundations](#-theoretical-foundations)
- [Repository Structure](#-repository-structure)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Examples](#-examples)
- [Benchmarking](#-benchmarking)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)
- [Citation](#-citation)

## Overview

The Semantic Holder (SH) primitive addresses a fundamental challenge in cryptographic systems: how to create outputs that are both cryptographically secure and legally meaningful. SH transforms computational results into legally binding interpretations with mathematically verifiable properties, maintaining a minimum opposability score of Ω ≥ 0.60 as proven in the accompanying paper.

SH completes the CASH framework triad:
- **Iron Layer (AOW)**: Temporal reliability and Byzantine resistance
- **Gold Layer (CEE)**: Data confidentiality and entropy preservation  
- **Clay Layer (SH)**: Legal opposability and verifiable interpretation

## Key Features

- **Provable Legal Opposability**: Mathematically guaranteed minimum opposability score Ω ≥ 0.60
- **Institutional Explainability**: Generation of institution-specific legal explanations
- **Legal Contestability**: Built-in mechanisms for dispute resolution pathways
- **Verifiable Computation**: STARK-proof verifiable computation of legal interpretations
- **Cross-Jurisdictional Support**: Configurable for multiple legal frameworks and jurisdictions
- **Quantum Resistance**: Security reductions to AIIP hardness with post-quantum security

## Theoretical Foundations

SH is built upon the **Affine Iterated Inversion Problem (AIIP)** with security reductions to:
1. Multivariate Quadratic (MQ) problem hardness
2. High-genus Hyperelliptic Curve Discrete Logarithm Problem (HCDLP)

The primitive maintains three core legal-theoretic properties:
1. **Explainability (Ε)**: Institutional clarity of legal interpretations
2. **Contestability (Γ)**: Availability of dispute resolution pathways  
3. **Verifiability (V)**: Cryptographic proof of correct computation

Formally, for legal interpretation L and jurisdiction J:
Ω(L, J) = min[ min{Ε(L, I), Γ(L, I), V(L)} ] for all institutions I ∈ J

## Repository Structure

```
semantic-holder/
├── src/                          # Source code
│   ├── core/                     # Cryptographic operations (AIIP, fields)
│   ├── legal/                    # Legal semantics and context handling
│   ├── proofs/                   # STARK proof integration
│   ├── types.py                  # Core data structures
│   └── utils.py                  # Helper functions
├── tests/                        # Comprehensive test suite
│   ├── unit/                     # Unit tests for components
│   ├── property/                 # Property-based tests
│   ├── integration/              # Integration tests
│   └── conftest.py               # Test configuration
├── examples/                     # Practical usage examples
│   ├── basic_extraction.py       # Basic AIIP iteration & mapping
│   ├── cross_jurisdiction.py     # Cross-jurisdictional interpretation
│   ├── opposability_verification.py # Ω calculation & verification
│   └── data/                     # Example contexts & verdict spaces
├── benchmarks/                   # Performance benchmarking
│   ├── scripts/                  # Benchmarking scripts
│   ├── configurations/           # Parameter configurations
│   ├── results/                  # Benchmark results
│   └── analysis/                 # Result analysis & visualization
├── docs/                         # Comprehensive documentation
│   ├── theory/                   # Theoretical explanations
│   ├── user-guide/               # Usage instructions
│   ├── api-reference/            # API documentation
│   └── tutorials/                # Step-by-step tutorials
├── assets/                       # Resources & templates
│   ├── images/                   # Diagrams & visualizations
│   ├── legal-templates/          # Legal configuration templates
│   └── parameters/               # Parameter sets
└── README.md                     # This file
```

## Installation

```bash
# Clone the repository
git clone https://github.com/KryptoResearcher/SH.git
cd SH

# Install in development mode
pip install -e .

# Install benchmarking dependencies (optional)
pip install -r benchmarks/requirements.txt
```

## Quick Start

```python
from src.core.fields import FiniteField
from src.core.aiip import compute_iteration_trace
from src.legal.mapping import semantic_map
from src.types import SHParameters

# Initialize parameters
params = SHParameters(
    field_size=1000003,  # Prime field size
    alpha=5,             # Quadratic non-residue
    iterations=10,       # Number of iterations
    security_param=80    # Security level
)

# Compute AIIP trace
field = FiniteField(params.field_size)
trace = compute_iteration_trace(123456, params.alpha, params.iterations, field)

# Map to legal verdict
verdict_space = ["Compliant", "Non-Compliant", "Further Investigation Needed"]
verdict = semantic_map(trace[-1], verdict_space, params.field_size)

print(f"Final verdict: {verdict}")
```

Run the basic example:
```bash
python examples/01_basic_extraction.py
```

## Examples

The repository includes several practical examples:

1. **Basic Extraction** (`examples/01_basic_extraction.py`):
   - Demonstrates core AIIP iteration and semantic mapping

2. **Cross-Jurisdictional Interpretation** (`examples/02_cross_jurisdiction.py`):
   - Shows how the same input produces different verdicts in different legal contexts

3. **Opposability Verification** (`examples/03_opposability_verification.py`):
   - Demonstrates calculation and verification of the opposability score Ω

4. **STARK Proof Integration** (`examples/04_stark_proofs.py`):
   - Placeholder for STARK proof integration example

## Benchmarking

The benchmarking suite allows performance assessment across different parameter configurations:


# Run AIIP performance benchmarks
python benchmarks/scripts/benchmark_aiip.py \
  -c benchmarks/configurations/small_params.json \
  -o benchmarks/results/current/aiip_small.csv

# Generate performance visualization
python benchmarks/analysis/plot_performance.py \
  -i benchmarks/results/current/aiip_small.csv \
  -o benchmarks/results/current/aiip_performance.png \
  -t time

# Generate comprehensive report
python benchmarks/analysis/generate_report.py \
  -c benchmarks/configurations/small_params.json \
  -i benchmarks/results/current/aiip_small.csv \
  -o benchmarks/results/current/report.md
```

Pre-configured parameter sets are available for:
- Development testing (`small_params.json`)
- Realistic assessment (`standard_params.json`) 
- Theoretical validation (`theoretical_params.json`)

## 📖 Documentation

Comprehensive documentation is available in the `/docs` directory:

- **Theory Guides**: Mathematical foundations and theoretical framework
- **User Guides**: Practical usage instructions and parameter configuration
- **API Reference**: Technical API documentation
- **Tutorials**: Step-by-step walkthroughs of examples

Key documentation files:
- [Theory Overview](/docs/theory/overview.md)
- [Installation Guide](/docs/user-guide/installation.md) 
- [Quick Start Guide](/docs/user-guide/quickstart.md)
- [Parameter Configuration](/docs/user-guide/parameters.md)

## 🤝 Contributing

As a research implementation, we welcome contributions from the academic community:

1. **Explore the Theory**: Read the accompanying paper and documentation
2. **Experiment with Code**: Run examples and explore the implementation
3. **Identify Issues**: Report bugs or theoretical concerns via GitHub Issues
4. **Suggest Enhancements**: Propose improvements to algorithms or documentation
5. **Submit Pull Requests**: Contribute code improvements or additional examples

Please see our [Contributing Guidelines](docs/contributing.md) and [Research Statement](docs/research.md) for more details.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📚 Citation

If you use this implementation in academic work, please cite the accompanying paper:


@article{sh2025,
  title={The Semantic Holder (SH): Algebraic Extraction for Legal Opposability},
  author={anonymised for doubleblind review},
  journal={anonymised for doubleblind review},
  year={2025},
  publisher={anonymised for doubleblind review}
}


## 🔮 Roadmap

Future work includes:

1. **Performance Optimization**: Migration of performance-critical components to Rust
2. **STARK Integration**: Full integration with a production-grade STARK prover
3. **Legal Framework Expansion**: Development of additional legal context templates
4. **Formal Verification**: Application of formal methods to verify implementation correctness
5. **Community Engagement**: Collaboration with legal and cryptographic research communities

---

For questions and discussions, please open an issue on GitHub or contact the research team. krytoresearcher@proton.me