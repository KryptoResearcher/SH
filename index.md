# Semantic Holder (SH) - Documentation

Welcome to the documentation for the Semantic Holder (SH) reference implementation. SH is a cryptographic primitive designed to provide **verifiable legal opposability** by transforming computational outputs into legally meaningful interpretations with mathematically proven guarantees.

## This is a Research Implementation

**Important:** This project is a **reference implementation** of a theoretical construct. It is intended for research, experimentation, and validation of the concepts presented in the accompanying academic paper. It is not yet audited or ready for production use.

## Documentation Overview

*   **Theory:** Start here if you want to understand the mathematical and legal-theoretic foundations of SH.
    *   [The SH Primitive: An Overview](/theory/overview.md)
    *   [The Affine Iterated Inversion Problem (AIIP)](/theory/aiip_problem.md)
    *   [Understanding Opposability (Ω)](/theory/opposability.md)

*   **User Guide:** Practical guides on installing and using the implementation.
    *   [Installation](/user_guide/installation.md)
    *   [Quick Start](/user_guide/quickstart.md)
    *   [Configuring Parameters](/user_guide/parameters.md)

*   **Tutorials:** Step-by-step walkthroughs of the provided examples.
    *   [Basic Extraction Tutorial](/tutorials/basic-extraction.md)
    *   [Cross-Jurisdictional Interpretation](/tutorials/cross-jurisdiction.md)

*   **API Reference:** Technical details of the codebase.
    *   [Core Module (AIIP, Fields)](/api-reference/core.md)
    *   [Legal Module (Mapping, Contexts)](/api-reference/legal.md)

## Getting Help

*   **Read the Paper:** The canonical source of truth is the academic paper.
*   **Explore the Examples:** The `/examples` directory is the best way to see SH in action.
*   **Open an Issue:** For bugs, questions, or suggestions, please open an issue on GitHub.