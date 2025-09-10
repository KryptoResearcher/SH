# Testing the Semantic Holder Primitive

This directory contains the test suite for the SH reference implementation. The tests are designed to validate both the correctness of the implementation and the theoretical properties described in the paper.

tests/
│
├── unit/                    # Tests for individual components and functions
│   ├── cor/
│   │   ├── test_fields.py
│   │   └── test_aiip.py
│   ├── legals/
│   │   ├── test_mapping.py
│   │   └── test_contexts.py
│   └── types/
│       └── test_types.py
│
├── property/                # Property-based tests (using hypothesis)
│   ├── test_property_aiip.py
│   └── test_property_mapping.py
│
├── integration/             # Tests for interactions between modules
│   ├── test_extraction_integration.py
│   └── test_opposability_integration.py
│
├── conftest.py              # Pytest configuration and shared fixtures
└── README.md                # Explanation of the testing strategy

## Testing Strategy

*   **Unit Tests:** Verify the behavior of individual functions and classes in isolation.
*   **Property-Based Tests:** Validate that key theoretical properties (e.g., entropy preservation, deterministic mapping) hold across a wide range of randomly generated inputs. This is crucial for a theoretical construct.
*   **Integration Tests:** Ensure that the different modules (`cor`, `legals`, `proofs`) work together correctly to produce the expected high-level output.

## Running the Tests

To run the entire test suite:
```bash
pytest -v

To run a specific subset of tests:
bash

pytest tests/unit/cor -v
pytest tests/property -v

Adding New Tests

When adding a new feature, please add corresponding unit and property-based tests.

    Unit tests should cover the happy path and key error conditions.

    Property-based tests should validate the abstract invariants of the system.


