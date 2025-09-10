# SH Primitive Benchmarking Suite

This directory contains tools and scripts for benchmarking the performance characteristics of the Semantic Holder primitive.

## Benchmarking Philosophy

As a theoretical construct, initial benchmarks focus on:
1.  **Algorithmic complexity** - Verifying theoretical time/space complexity
2.  **Implementation overhead** - Measuring constant factors in our implementation
3.  **Component analysis** - Isolating performance of individual components

## Quick Start

1.  Install benchmarking dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Run a basic benchmark:
    ```bash
    python scripts/benchmark_aiip.py -c configurations/small_params.json -o results/current/aiip_small.csv
    ```

3.  Generate visualizations:
    ```bash
    python analysis/plot_performance.py -i results/current/aiip_small.csv -o results/current/aiip_performance.png
    ```

## Benchmark Types

1.  **Time Performance:** Measures execution time of core operations
2.  **Memory Usage:** Tracks memory consumption during operations
3.  **Scalability:** Tests performance across parameter sizes
4.  **Component Breakdown:** Isolates performance of different SH components

## Parameters

Benchmarks use parameter sets defined in `configurations/`:
- `small_params.json`: For rapid development testing (small numbers)
- `standard_params.json`: For more realistic performance assessment
- `theoretical_params.json`: Parameters matching the paper's recommendations

## Results Format

Benchmarks output CSV files with columns:
- `timestamp`: When benchmark was run
- `parameter_set`: Which configuration was used
- `operation`: What was measured (e.g., "aiip_iteration")
- `input_size`: Size of input data
- `iteration_count`: Number of AIIP iterations
- `field_size`: Size of finite field
- `execution_time_ms`: Execution time in milliseconds
- `memory_usage_kb`: Peak memory usage in kilobytes
- `additional_metrics`: Operation-specific metrics

## Example Benchmarking Workflow

    Developmental Testing:
    bash

python scripts/benchmark_aiip.py -c configurations/small_params.json -o results/current/aiip_small.csv
python analysis/plot_performance.py -i results/current/aiip_small.csv -o results/current/aiip_small.png -t time

Comprehensive Assessment:
bash

python scripts/benchmark_aiip.py -c configurations/standard_params.json -o results/current/aiip_standard.csv
python scripts/benchmark_memory.py -c configurations/standard_params.json -o results/current/memory_standard.csv
python analysis/plot_performance.py -i results/current/aiip_standard.csv -o results/current/aiip_standard.png -t time
python analysis/plot_performance.py -i results/current/memory_standard.csv -o results/current/memory_standard.png -t memory
python analysis/generate_report.py -c configurations/standard_params.json -i results/current/aiip_standard.csv results/current/memory_standard.csv -o results/current/report.md

## End Notes
This benchmarking infrastructure will provide the empirical data needed to:

    Validate the theoretical complexity claims from the paper

    Identify performance bottlenecks in the implementation

    Guide optimization efforts (especially when porting to Rust/C++)

    Provide concrete performance numbers for future publications or technical reports

The structure is designed to grow with the project, from initial Python prototyping to eventual production-ready implementation.
