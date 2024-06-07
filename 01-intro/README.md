# Intro to the ML task (homework 1)
## Files
- `homework_instructions.md` - instructions by DTC + answered questions
- `homework.ipynb` - code verifying the answers
- `README.md` - instructions on how to run the code
- `requirements.txt` - requirements file to create the code environment
- `data/yellow_tripdata_2023-01.parquet` - yellow taxi trip records from January 2023 (used as the training set)
- `data/yellow_tripdata_2023-02.parquet` - yellow taxi trip records from February 2023 (used as the validation set)

## Pre-requirements to run the code
- Go into homework 1 folder (if not already)
    ```
    cd 01-intro
    ```
- Create conda environment
    ```
    conda create -n hw1 python==3.12.3
    conda activate hw1
    pip install -r requirements.txt
    ```

## How to run the code
- Go into homework 1 folder (if not already)
    ```
    cd 01-intro
    ```
- Activate conda environment (if not already)
    ```
    conda activate hw1
    ```
- Run
    ```
    jupyter notebook
    ```
