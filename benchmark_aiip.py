#!/usr/bin/env python3
"""
Benchmark script for AIIP iteration performance.
Measures time and memory usage for computing AIIP traces.
"""

import time
import timeit
import json
import csv
import sys
sys.path.append('../..')

from src.core.fields import FiniteField
from src.core.aiip import compute_iteration_trace
from memory_profiler import memory_usage

def benchmark_aiip(config):
    """Run AIIP performance benchmarks with given configuration."""
    
    results = []
    
    for field_size in config['field_sizes']:
        field = FiniteField(field_size)
        
        for alpha in config['alpha_values']:
            for iterations in config['iteration_counts']:
                print(f"Benchmarking: q={field_size}, α={alpha}, n={iterations}")
                
                # Use a fixed test value
                test_input = 123456
                
                # Time measurement
                def time_func():
                    return compute_iteration_trace(test_input, alpha, iterations, field)
                
                # Warmup runs
                for _ in range(config['warmup_runs']):
                    time_func()
                
                # Time benchmark
                timer = timeit.Timer(time_func)
                time_results = timer.repeat(
                    repeat=config['runs_per_config'], 
                    number=1
                )
                
                # Memory benchmark
                mem_usage = memory_usage(
                    (time_func,),
                    interval=0.1,
                    max_usage=True
                )
                
                # Record results
                for i, time_ms in enumerate(time_results):
                    results.append({
                        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                        'parameter_set': config['name'],
                        'operation': 'aiip_iteration',
                        'field_size': field_size,
                        'alpha': alpha,
                        'iteration_count': iterations,
                        'execution_time_ms': time_ms * 1000,  # Convert to milliseconds
                        'memory_usage_kb': mem_usage * 1024,  # Convert to kilobytes
                        'additional_metrics': f"run_{i+1}"
                    })
    
    return results

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Benchmark AIIP iteration performance')
    parser.add_argument('-c', '--config', required=True, help='Configuration JSON file')
    parser.add_argument('-o', '--output', required=True, help='Output CSV file')
    
    args = parser.parse_args()
    
    # Load configuration
    with open(args.config, 'r') as f:
        config = json.load(f)
    
    # Run benchmarks
    results = benchmark_aiip(config)
    
    # Write results
    with open(args.output, 'w', newline='') as f:
        if results:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writeheader()
            writer.writerows(results)
    
    print(f"Benchmark results written to {args.output}")

if __name__ == "__main__":
    main()