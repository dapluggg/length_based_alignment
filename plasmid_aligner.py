
# Shashank Nagaraja, Feb 15th, 2025

import sys 
import os
import argparse
import subprocess

def subset_by_read_length(fastq, reference_length, length_wiggle, output):
    """
    Subset reads by reference_length +/- length_wiggle.
    """
    # Create output directory
    os.makedirs(output, exist_ok=True)

    # Subset reads by length
    subset_fastq = os.path.join(output, "subset.fastq")
    with open(fastq, "r") as f_in, open(subset_fastq, "w") as f_out:
        for line1 in f_in:
            line2 = next(f_in)
            line3 = next(f_in)
            line4 = next(f_in)
            read_length = len(line2.strip())
            if reference_length - length_wiggle <= read_length <= reference_length + length_wiggle:
                f_out.write(line1)
                f_out.write(line2)
                f_out.write(line3)
                f_out.write(line4)

    return subset_fastq

def run_unicycler(subset_fastq, output):
    """
    Run Unicycler on the subset of reads. First load unicycler using 'module load unicycler'
    """
    # Run Unicycler
    subprocess.run([
        "unicycler",
        "-l", subset_fastq,
        "-o", output
    ])
    return output

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Align plasmid reads to reference plasmid using Unicycler")
    parser.add_argument("--fastq", help="Path to the fastq file from nanopore sequencing of plasmid", required=True)
    parser.add_argument("--reference_length", type=int, help="Known length of the reference plasmid", required=True)
    parser.add_argument("--length_wiggle", type=int, help="Allowed wiggle room for the length of the plasmid. Default=1000", default=1000)
    parser.add_argument("--output", help="Path to the desired output directory", required=True)
    args = parser.parse_args()

    # Subset reads by length
    subset_fastq = subset_by_read_length(args.fastq, args.reference_length, args.length_wiggle, args.output)

    # Run Unicycler
    run_unicycler(subset_fastq, args.output)

if __name__ == "__main__":
    main()