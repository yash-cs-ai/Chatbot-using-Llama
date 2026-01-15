# List of commands used for environment and basic setup

1. Creating venv via Conda

    ```bash
    conda create -n venv_name python=3.8
    ```

2. To activate or deactivate venv

    ```bash
    conda activate venv_name
    ```

    ```bash
    conda deactivate
    ```

3. Install dependencies
    Create a requirement.txt file containing your required libararies and use the command

    ```bash
    pip install -r requirements.txt
    ```

4. Model installation and information

    refer to model [instruction folder](../model/modelinfo.md)

5. Data setup
    Add your data source in to the [Data folder](/data/) folder this case, I've used a medical encyclopedia.

6. Write the code from [Code source](../research/maincode.ipynb) and run it.
