import os
import shutil

from setuptools import setup

with open(os.path.join("mle_zoo3", "version.txt")) as file_handler:
    __version__ = file_handler.read().strip()

# Copy hyperparams files for packaging
shutil.copytree("hyperparams", os.path.join("mle_zoo3", "hyperparams"))

long_description = """
# RL Baselines3 Zoo: A Training Framework for Stable Baselines3 Reinforcement Learning Agents
With modifications by MLE

See https://github.com/loganetherton/rl-baselines3-zoo
"""

setup(
    name="mle_zoo3",
    packages=["mle_zoo3", "mle_zoo3.plots"],
    package_data={
        "mle_zoo3": [
            "py.typed",
            "version.txt",
            "hyperparams/*.yml",
        ]
    },
    entry_points={"console_scripts": ["mle_zoo3=mle_zoo3.cli:main"]},
    install_requires=[
        "sb3_contrib>=2.0.0a9",
        "gym==0.26.2",
        "huggingface_sb3>=2.2.1",
        "tqdm",
        "rich",
        "optuna",
        "pyyaml>=5.1",
        "pytablewriter~=0.64",
        # TODO: add test dependencies
    ],
    extras_require={
        "plots": ["seaborn", "rliable>=1.0.5", "scipy~=1.7.3"],
    },
    description="A Training Framework for Stable Baselines3 Reinforcement Learning Agents",
    author="Antonin Raffin",
    url="https://github.com/loganetherton/rl-baselines3-zoo",
    author_email="antonin.raffin@dlr.de",
    keywords="reinforcement-learning-algorithms reinforcement-learning machine-learning "
    "gym gymnasium openai stable baselines sb3 toolbox python data-science",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version=__version__,
    python_requires=">=3.7",
    # PyPI package information.
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)

# Remove copied files after packaging
shutil.rmtree(os.path.join("mle_zoo3", "hyperparams"))


# python setup.py sdist
# python setup.py bdist_wheel
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# twine upload dist/*
