#!/usr/bin/env python3
"""
Example 2: Cross-Jurisdictional Interpretation
Shows how the same input produces different verdicts in different contexts.
"""

import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.core.fields import FiniteField
from src.core.aiip import compute_iteration_trace
from src.legal.mapping import semantic_map
from src.types import SHParameters, RelationalContext

def load_context(context_name):
    """Helper to load a RelationalContext from JSON."""
    context_path = os.path.join('data', 'contexts', f"{context_name}.json")
    with open(context_path, 'r') as f:
        data = json.load(f)
    return RelationalContext(**data)

def main():
    print("=== Example 2: Cross-Jurisdictional Interpretation ===\n")
    
    # Use the same cryptographic input and parameters
    input_data = 123456
    params = SHParameters(
        field_size=1000003,
        alpha=5,
        iterations=10,
        security_param=80
    )
    field = FiniteField(params.field_size)
    trace = compute_iteration_trace(input_data, params.alpha, params.iterations, field)
    final_element = trace[-1]
    
    print(f"Consistent Cryptographic Output: {final_element}\n")
    
    # Demonstrate different interpretations across contexts
    contexts = {
        'corporate_audit': "Corporate Tax Audit (US)",
        'personal_dispute': "Personal Data Dispute (EU)",
        'public_compliance': "Public Procurement Compliance (UK)"
    }
    
    for context_key, context_description in contexts.items():
        # Load the context and its verdict space
        context = load_context(context_key)
        verdict = semantic_map(final_element, context.verdict_space, params.field_size)
        
        print(f"Context: {context_description}")
        print(f"  Jurisdiction: {context.jurisdiction}")
        print(f"  Legal Framework: {context.legal_framework}")
        print(f"  Interpretation: '{verdict}'")
        print()

if __name__ == "__main__":
    main()