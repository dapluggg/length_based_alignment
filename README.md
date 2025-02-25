# Length-Based Alignment: A Quick Solution for Whole Plasmid Sequence Assembly

## Introduction
When sequencing plasmids using third-party services (e.g., Eurofins, Plasmidsaurus), the assemblies generated from Nanopore reads can sometimes be inaccurate. These providers often utilize minimal alignment parameters and do not always know the true length of the plasmid. As a result:

- **Shorter reads** tend to align preferentially to a smaller, truncated plasmid assembly.
- **Longer reads** may be duplicated in the final alignment, leading to an assembly that appears to be two or three times larger than the actual plasmid.

However, researchers often know the correct plasmid length from additional validation steps (e.g., restriction enzyme digests). This discrepancy between expected and computed lengths can cause significant confusion and complicate downstream analyses.

## Purpose of This Tool
This Python script addresses the issue of misalignment by filtering FASTQ reads to include only those consistent with the known plasmid length (within a user-specified tolerance). By focusing on reads of the appropriate length, the script prevents incorrect or duplicated fragments from distorting the final assembly.

**Installation and Requirements**

```bash
module load python
module load unicycler
```
   
**Clone the GitHub repository:**

```bash
git clone https://github.com/dapluggg/length_based_alignment.git
```
   
**Print out the help message:**

```bash
python plasmid_aligner.py --help
```
   
**Run the script with appropriate parameters:**

```bash
python plasmid_aligner.py \
  --fastq /path/to/your/fastq/from/wholeplasmidseq/ \
  --reference_length 9600 \
  --length_wiggle 1000 \
  --output /path/to/your/output/directory/
```
