# Cookiecutter CompBio

A [rpazuki/cookiecutter-compbio](https://github.com/rpazuki/cookiecutter-compbio) template for computational biology projects.

---

# Quickstart

* Install cookiecutter

`pip install -U cookiecutter`

Or:

`conda install -c conda-forge cookiecutter`

* Initialize the project

`cookiecutter https://github.com/rpazuki/cookiecutter-compbio.git`

* Create the enviroment and start working!

`conda env create --file environment.yml`

* for each new numerical experiment, enter the experiments folder, and create a new one

`cd expriments`

`cookiecutter template`

* To use the newer version of the template on old projects, use
`cookiecutter https://github.com/rpazuki/cookiecutter-compbio.git --replay  -f`


---
# Workflow Initiation

### The Ideal Workflow

The ideal workflow should meet the following expectations. While not all are currently prioritized, the top items in the list are the most important for now:

1. Each numerical experiment must be **self-contained**, including its data, algorithms, libraries, and results.
2. Each experiment should be **self-explanatory** for the same researcher in the future.
3. Results must be **reproducible**.
4. The entire study, including all experiments, should be understandable to other researchers if shared.
5. The workflow should support **easy extraction** of key elements (e.g., plotting scripts and data) for publication or submission.
6. **Sharing** mechanisms are still under consideration.

---

### Workflow Folder Structure

The workflow is organized into the following main folders. Some include subfolders, whose purposes are explained below:

1. **`data/`**  
    Contains all experimental data. Subfolders may be used to logically categorize lab data, though no strict naming convention is enforced at this stage. All numerical experiments will access this folder directly, ensuring a single copy of raw data exists locally. For shared or remote access, this folder can use **mounting** or **symbolic links** to point to the appropriate data source.
    
2. **`docs/`**  
    Stores files related to paper submissions. Subfolders may be used to organize content by paper title, journal formatting, or revision stage. No naming conventions are currently enforced.
    
3. **`src/`**  
    Contains general-purpose code developed by researchers. All experiments should treat this folder as a local library. This promotes code reuse, consistency, and easier development. Ideally, this folder will be maintained in a shared repository for use in future projects.
    
4. **`experiments/`**  
    This folder holds all numerical experiments. Each experiment should be placed in a subfolder named using the format:  
    **`PersonName_Date_ShortDescription`**  
    The date helps track chronological order, assuming each experiment spans several days.
    
    Each experiment folder must be **self-contained and reproducible**. It should include:
    
    - A dedicated **Python environment** to avoid version conflicts. Use `pip freeze` to capture dependencies for future use.
    - **`README.md`** – Describes the experiment.
    - **`Makefile`** – Automates key steps.
    - **`processed/`** – Contains preprocessed data. Raw data is read from `data/` and saved here. All preprocessing steps should be implemented in a single script or notebook, executable via `make`.
    - **`notebooks/`** – Jupyter notebooks. Use a naming convention:  
        `number-initials-description`, e.g., `1.0-jqp-initial-data-exploration`.
    - **`models/`** – Stores trained models, predictions, and summaries.
    - **`reports/`** – Contains generated outputs (e.g., HTML, PDF, LaTeX), including figures.
    
    Additionally:
    
    - A **`log_book`** file should be maintained in the `experiments/` folder. It should briefly describe the project goals and each experiment. Entries can be added before and/or after an experiment. Writing at both stages is encouraged to compare expectations with outcomes.
    - A **`requirements.txt`** file should be included to capture the environment (e.g., via `pip freeze > requirements.txt`).
    - The experiment should be executable via `make`, with at least the following steps:
        - **Preprocessing** – Processes raw data.
        - **Modeling** – Includes training, fitting, transforming, etc. Key outputs (e.g., CSVs, plots) should be saved in the `reports/` folder.
    
    Creating a new experiment should be straightforward. A script should be provided to either:
    
    - Generate an empty folder structure, or
    - Duplicate an existing experiment as a starting point.

---
### Disclaimer

The following workflow is inspired by ideas from [https://doi.org/10.1371/journal.pcbi.1000424](https://doi.org/10.1371/journal.pcbi.1000424), [https://davetang.org/muse/2018/02/09/organising-computational-biology-projects-cookiecutter/](https://davetang.org/muse/2018/02/09/organising-computational-biology-projects-cookiecutter/), the [https://cookiecutter.readthedocs.io/en/latest/](https://cookiecutter.readthedocs.io/en/latest/) tool, the [https://cookiecutter-data-science.drivendata.org/](https://cookiecutter-data-science.drivendata.org/) philosophy, and personal experience.

---