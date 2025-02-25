# Quick Program to Fix Whole Plasmid Sequence Alignment

Whole plasmid sequencing providers (e.g., Eurofins, Plasmidsaurus) often run a very basic alignment of the Nanopore reads. Since they do not know the actual length of the plasmid, their assembly is often incorrect because smaller fragments will more efficiently align into a smaller, incomplete genome. Worse, sometimes larger fragments may align as duplicates, causing the final assembly to appear two or three times larger than the actual plasmid. Typically, the true length of the plasmid is confirmed via a restriction enzyme digest.

This program addresses the issue by subsetting the FASTQ reads to those that match the known plasmid length (+/- a defined wiggle room).

---

## Usage

1. **Install the requirements on UF HiperGator:**

    ```bash
    module load python
    module load unicycler
    ```
   
2. **Clone the GitHub repository:**

    ```bash
    git clone https://github.com/dapluggg/length_based_alignment.git
    ```
   
3. **Print out the help message:**

    ```bash
    python plasmid_aligner.py --help
    ```
   
4. **Run the script with appropriate parameters:**

    ```bash
    python plasmid_aligner.py \
      --fastq /path/to/your/fastq/from/wholeplasmidseq/ \
      --reference_length 9600 \
      --length_wiggle 1000 \
      --output /path/to/your/output/directory/
    ```
