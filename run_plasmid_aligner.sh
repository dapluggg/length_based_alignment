module load python ;
module load unicycler ;

python plasmid_aligner.py \
--fastq /path/to/your/fastq/from/wholeplasmidseq/ \
--reference_length 9600 \
--length_wiggle 1000 \
--output /path/to/your/output/directory/ ;