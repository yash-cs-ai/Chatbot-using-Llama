# List of commands used for environment and basic setup

Before starting you, can use instructions from [tools and libaries](toolsandlib.md) on what applications or softwares were used.

1. Creating venv via Conda

    ```bash
    conda create -n venv_name python=3.8
    ```

2. to activate or deactivate venv

    ```bash
    conda activate venv_name
    ```

    ```bash
    conda deactivate
    ```

3. install dependencies
    Create a requirement.txt file containing your required libararies and use the command

    ```bash
    pip install -r requirements.txt
    ```

4. model installation and information

    refer to model [instruction folder](../model/modelinfo.md)

5. data setup
    Add your data source in to the [Data folder](/data/) folder this case, I've used a medical encyclopedia.

6. Write the code from [Code source](../maincode.ipynb) and run it.
