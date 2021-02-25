
### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install --user cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

python -m  cookiecutter <URL>


### The resulting directory structure
------------

```
├── README.md <- The top-level README for developers using this project.
├── venv/      <- Virtual env, add to .gitignore
├── data
│ ├── output <- Data from third party sources.
│ ├── interim <- Intermediate data that has been transformed.
│ └── raw/input <- The original, immutable data dump.
├── docs <- A default Sphinx project, reports, Dataviz Spotfire
├── notebooks <- Jupyter notebooks. 
│ ├── experiments <- Notebooks store during experimentation 
│ ├── features <- features developped in notebooks
│ ├── models <- model notebooks
├── requirements.txt <- The requirements file for reproducing the analysis environment
├── setup.py <- makes project pip installable (pip install -e .) so "datalab" can be imported
├── datalab <- Source code for use in this project.
│ ├── __init__.py <- Makes datalab a Python package
| |
│ ├── source <- Scripts to download or generate data
│ │ └── fetch_dataset.py <- Scripts to populates the raw directory
│ │
│ ├── features <- Scripts to turn raw data into features for modeling
│ │ └── build_features.py
│ │
│ ├── models <- Scripts to train models and then use trained models to make
│ │ │ predictions
│ │ ├── predict_model.py
│ │ └── train_model.py
│ │
│ └── visualization <- Scripts to create exploratory and results oriented visualizations
│ |  └── visualize.py
| |
│ ├── utils/   <- Util functions used in source, preprocess, model. 
│ ├── main.py <- Entry point for running the algorithm
| ├── tests/ < Unit tests
|  
└─ .gitignore <- Give rules of file that should not be versionned
```