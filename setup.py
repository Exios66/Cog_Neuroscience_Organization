from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read().splitlines()

setup(
    name="cog_neuro",
    version="0.1.0",
    author="Cognitive Neuroscience Organization",
    author_email="contact@example.com",
    description="Tools and resources for cognitive neuroscience research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Exios66/Cog_Neuroscience_Organization",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Intended Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.2.0",
            "pytest-cov>=2.12.0",
            "black>=21.6b0",
            "flake8>=3.9.0",
            "mypy>=0.910",
        ],
        "docs": [
            "mkdocs>=1.2.0",
            "mkdocs-material>=7.3.0",
        ],
    },
) 