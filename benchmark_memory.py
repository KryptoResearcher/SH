#!/usr/bin/env python3
"""
Benchmark script for memory usage of complete SH extraction.
"""

import json
import csv
import time
from memory_profiler import memory_usage
sys.path.append('../..')

from src.core.fields import FiniteField
from src.core.aiip import compute_iteration_trace
from src.legal.mapping import semantic_map

def benchmark_memory(config):
    """Benchmark memory usage of complete SH extraction."""
    
    results = []
    
    for field_size in config['field_sizes']:
        field = FiniteField(field_size)
        
        for alpha in config['alpha_values']:
            for iterations in config['iteration_counts']:
                for verdict_space_size in config['verdict_space_sizes']:
                    print(f"Benchmarking: q={field_size}, α={alpha}, n={iterations}, |V|={verdict_space_size}")
                    
                    # Create a verdict space
                    verdict_space = [f"Verdict_{i}" for i in range(verdict_space_size)]
                    test_input = 123456
                    
                    def extraction_process():
                        # Complete SH extraction process
                        trace = compute_iteration_trace(test_input, alpha, iterations, field)
                        verdict = semantic_map(trace[-1], verdict_space, field_size)
                        return trace, verdict
                    
                    # Memory profiling
                    mem_usage = memory_usage(
                        (extraction_process,),
                        interval=0.1,
                        max_usage=True,
                        include_children=True
                    )
                    
                    results.append({
                        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                        'parameter_set': config['name'],
                        'operation': 'complete_extraction',
                        'field_size': field_size,
                        'alpha': alpha,
                        'iteration_count': iterations,
                        'verdict_space_size': verdict_space_size,
                        'memory_usage_kb': mem_usage * 1024,
                        'additional_metrics': 'peak_usage'
                    })
    
    return results

# (Similar structure to benchmark_aiip.py for main() and CSV output)