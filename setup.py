from setuptools import setup, find_packages

__version__ = "1.0"
setup(
    name="nlp-examples",
    version=__version__,
    python_requires=">=3.9,<3.13",
    install_requires=[
        "nltk==3.6.2",
        "pandas==2.2.2",
        "pytorch-lightning==2.2.5",
        "sentencepiece==0.2.0",
        "spacy==3.7.4",
        "symspellpy==6.7.6",
        "protobuf==3.20.3",  # required for deberta-v3 tokenizer
        "transformers==4.41.2",
        "tqdm==4.66.4",
    ],
    extras_require={
        "lint": [
            "black==24.2.0",
            "isort==5.13.2",
            "pre-commit==3.6.1",
            "flake8==7.0.0",
            "mypy==1.8.0",
        ],
        "notebook": ["jupyterlab==4.0.11", "ipywidgets==8.1.1", "seaborn==0.12.2"],
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
