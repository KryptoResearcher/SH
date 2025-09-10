# User Guide: Quick Start

This guide will walk you through running your first SH extraction.

## Prerequisites

*   Python 3.8+
*   pip

## 1. Installation

Clone the repository and install the package in development mode:

bash
git clone https://github.com/KryptoResearcher/SH.git
cd semantic-holder
pip install -e .

## 2. Run the Basic Example

The fastest way to see SH in action is to run the basic extraction example.
bash

python examples/01_basic_extraction.py

You should see output similar to:
text

=== Example 1: Basic SH Extraction ===

Input data (hash): 123456
Field size (q): 1000003
Alpha (α): 5
Iterations (n): 10

Final field element (fⁿ(h)): 742042

Mapped Verdict: 'Further Investigation Needed'
Verdict Space: ['Compliant', 'Non-Compliant', 'Further Investigation Needed', 'Inconclusive']

## 3. What Happened?

    The example took an input number (123456).

    It iteratively applied the function f(x) = x² + 5 modulo 1000003 for 10 steps.

    It took the final, seemingly random result (742042).

    It mapped this number into a simple legal verdict space, selecting 'Further Investigation Needed'.

This demonstrates the core flow: input -> iterative computation -> semantic mapping -> verdict.
Next Steps

    Modify the Example: Change the input_data, alpha, or iterations in 01_basic_extraction.py and see how the verdict changes.

    Cross-Jurisdiction: Run 02_cross_jurisdiction.py to see how the same input leads to different verdicts in different legal contexts.

    Learn about Parameters: Understand how to choose strong parameters for real-world use cases in the Parameters Guide.

text



