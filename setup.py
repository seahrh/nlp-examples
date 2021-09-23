from setuptools import setup, find_packages

__version__ = "1.0"
setup(
    name="nlp-examples",
    version=__version__,
    python_requires="~=3.7",
    install_requires=[
        "nltk==3.6.2",
        "pandas==1.3.2",
        "pytorch-lightning==1.4.4",
        "sentencepiece==0.1.96",
        "spacy==3.1.2",
        "transformers==4.9.2",
        "tqdm==4.62.2",
    ],
    extras_require={
        "tests": [
            "black==20.8b1",
            "mypy==0.812",
            "pytest==6.2.3",
            "pytest-cov==2.11.1",
        ],
        "notebook": ["jupyterlab==1.2.16", "seaborn==0.11.1", "ipywidgets==7.6.3"],
    },
    packages=find_packages("src", exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_dir={"": "src"},
    include_package_data=True,
    description="NLP code examples",
    license="MIT",
    author="seahrh",
    author_email="seahrh@gmail.com",
    url="https://github.com/seahrh/nlp-examples",
)
