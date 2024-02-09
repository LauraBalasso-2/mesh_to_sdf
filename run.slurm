#!/bin/sh

#SBATCH -q develop
#SBATCH -p develop
#SBATCH -t 01:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --ntasks-per-core=1
#SBATCH --mem=20GB
#SBATCH --hint=nomultithread
#SBATCH -J mesh_to_sdf
#SBATCH -e job.%J.err
#SBATCH -o job.%J.out


#load modules
module purge

#****
# FROM SUBMIT DIR
cd $SLURM_SUBMIT_DIR

source /home/laura/Programs/miniconda3/etc/profile.d/conda.sh
export PATH="home/laura/Programs/miniconda3/bin:$PATH"
export PYTHONPATH="/home/laura/source/Github_repos/optimad/Rombox-devel/rombox/build/python-wrapper/:$PYTHONPATH"
export LD_LIBRARY_PATH="/home/laura/source/Github_repos/optimad/Rombox-devel/rombox/build/:$LD_LIBRARY_PATH"

conda activate mesh2sdf

OMP_NUM_THREADS=4 python example/prova.py


#*******
