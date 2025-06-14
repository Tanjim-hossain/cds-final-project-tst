#!/bin/bash -l
#SBATCH --job-name=tst_benchmark
#SBATCH --output=tst_benchmark_%j.out
#SBATCH --error=tst_benchmark_%j.err
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=genius
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
#SBATCH --time=00:15:00


echo "==== TST BENCHMARK JOB START ===="
echo "Job ID: $SLURM_JOB_ID"
echo "Host: $(hostname)"
echo "Started at: $(date)"
echo "Current directory: $(pwd)"

python3 benchmark_tst.py

echo "==== TST BENCHMARK JOB END ===="
echo "Ended at: $(date)"