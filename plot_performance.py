#!/usr/bin/env python3
"""
Script for generating performance visualizations from benchmark results.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def plot_aiip_performance(input_file, output_file):
    """Generate performance plots for AIIP iteration."""
    
    # Load data
    df = pd.read_csv(input_file)
    
    # Set style
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Create plot
    plot = sns.lineplot(
        data=df, 
        x='iteration_count', 
        y='execution_time_ms', 
        hue='field_size',
        style='field_size',
        markers=True,
        dashes=False
    )
    
    plt.title('AIIP Iteration Performance')
    plt.xlabel('Number of Iterations (n)')
    plt.ylabel('Execution Time (ms)')
    plt.legend(title='Field Size (q)')
    plt.yscale('log')  # Use log scale if times vary widely
    
    # Save plot
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

def plot_memory_usage(input_file, output_file):
    """Generate memory usage plots."""
    
    df = pd.read_csv(input_file)
    
    plt.figure(figsize=(10, 6))
    plot = sns.lineplot(
        data=df,
        x='iteration_count',
        y='memory_usage_kb',
        hue='field_size',
        style='field_size',
        markers=True,
        dashes=False
    )
    
    plt.title('Memory Usage of AIIP Iteration')
    plt.xlabel('Number of Iterations (n)')
    plt.ylabel('Peak Memory Usage (KB)')
    plt.legend(title='Field Size (q)')
    
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

def main():
    parser = argparse.ArgumentParser(description='Generate performance visualizations')
    parser.add_argument('-i', '--input', required=True, help='Input CSV file')
    parser.add_argument('-o', '--output', required=True, help='Output image file')
    parser.add_argument('-t', '--type', choices=['time', 'memory'], required=True, help='Plot type')
    
    args = parser.parse_args()
    
    if args.type == 'time':
        plot_aiip_performance(args.input, args.output)
    elif args.type == 'memory':
        plot_memory_usage(args.input, args.output)
    
    print(f"Plot saved to {args.output}")

if __name__ == "__main__":
    main()