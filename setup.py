import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification-Deep-Learning-Project"
AUTHOR_USER_NAME = "Sgurung14"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "safin8312@hotmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A deep learning project to classify kidney tumors as benign or cancerous using machine learning techniques on Kidney CT Scan images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "tensorflow==2.12.0",
        "pandas",
        "dvc",
        "mlflow==2.2.2",
        "notebook",
        "numpy",
        "matplotlib",
        "seaborn",
        "python-box==6.0.2",
        "pyYAML",
        "tqdm",
        "ensure==1.0.2",
        "joblib",
        "types-PyYAML",
        "scipy",
        "Flask",
        "Flask-Cors",
        "gdown",
    ],
)