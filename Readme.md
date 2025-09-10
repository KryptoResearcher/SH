# Semantic Holder (SH) - Examples

This directory contains practical examples demonstrating the functionality of the Semantic Holder primitive.

## Example Scripts

1.  **`01_basic_extraction.py`**  
    Demonstrates the core AIIP iteration and the semantic mapping function φ. Shows how a hash is transformed into a legal verdict.

2.  **`02_cross_jurisdiction.py`**  
    Shows how the same initial input data leads to different legal interpretations when processed under different relational contexts (jurisdictions and frameworks).

3.  **`03_opposability_verification.py`**  
    Demonstrates the calculation of the opposability score Ω and the verification of the minimum bound (Ω ≥ 0.60).

4.  **`04_stark_proofs.py`**  
    *(Placeholder)* Illustrates the integration with a STARK proof system to generate and verify computational integrity proofs.

## Data Files

The `data/` directory contains sample configuration files:
- `contexts/`: JSON files defining `RelationalContext` parameters.
- `verdict_spaces/`: Text files listing possible verdicts for different legal domains.

## Running the Examples

1.  Install dependencies:  
    `pip install -r requirements.txt`

2.  Run any example:  
    `python 01_basic_extraction.py`