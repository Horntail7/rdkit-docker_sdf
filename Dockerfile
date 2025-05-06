# Dockerfile
FROM continuumio/miniconda3

# Create a Conda environment with RDKit
RUN conda create -y -n rdkit_env -c rdkit -c conda-forge rdkit python=3.9

# Activate the environment by default
SHELL ["conda", "run", "-n", "rdkit_env", "/bin/bash", "-c"]

# Optional: copy your RDKit script into the container
COPY rdkit_script-sdf.py /app/rdkit_script-sdf.py

WORKDIR /app

CMD ["conda", "run", "-n", "rdkit_env", "python", "rdkit_script-sdf.py"]
