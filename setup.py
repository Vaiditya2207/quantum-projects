"""Setup script for quantumsim advanced educational quantum simulator."""

from setuptools import setup, find_packages
import os

# Read README from quantumsim subdirectory
readme_path = os.path.join("quantumsim", "README.md")
if os.path.exists(readme_path):
    with open(readme_path, "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = "Advanced Educational Quantum Computing Simulator with ML, Visualization, and Optimization"

# Read requirements from quantumsim subdirectory
req_path = os.path.join("quantumsim", "requirements.txt")
if os.path.exists(req_path):
    with open(req_path, "r", encoding="utf-8") as fh:
        requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
else:
    requirements = [
        "numpy>=1.21.0",
        "matplotlib>=3.5.0", 
        "scipy>=1.7.0",
        "jupyter>=1.0.0"
    ]

setup(
    name="quantumsim-edu",
    version="2.0.0",
    author="Vaiditya Tanwar",
    author_email="vaiditya2207@gmail.com",
    description="Advanced Educational Quantum Computing Simulator with ML and Optimization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vaiditya2207/quantum-projects",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research", 
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9", 
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "jupyter": ["jupyter", "matplotlib", "plotly", "ipywidgets"],
        "dev": ["pytest", "black", "flake8", "mypy", "pytest-cov"],
        "full": ["qiskit>=0.44.0", "cirq>=1.0.0", "plotly>=5.0.0", "seaborn>=0.11.0"],
    },
    entry_points={
        "console_scripts": [
            "quantumsim=quantumsim.cli:main",
            "quantumsim-demo=quantumsim.examples.demo_advanced_features:main",
        ],
    },
    include_package_data=True,
    package_data={
        "quantumsim": [
            "tutorials/*.ipynb",
            "docs/*.md", 
            "examples/*.py",
            "README.md"
        ],
    },
    keywords=[
        "quantum computing",
        "education", 
        "simulation",
        "qubits",
        "quantum circuits",
        "quantum algorithms",
        "quantum machine learning",
        "error correction",
        "visualization",
        "research",
        "physics"
    ],
    project_urls={
        "Documentation": "https://github.com/Vaiditya2207/quantum-projects/blob/main/README.md",
        "Source": "https://github.com/Vaiditya2207/quantum-projects",
        "Tutorials": "https://github.com/Vaiditya2207/quantum-projects/tree/main/quantumsim/tutorials",
        "Examples": "https://github.com/Vaiditya2207/quantum-projects/tree/main/quantumsim/examples",
        "Bug Reports": "https://github.com/Vaiditya2207/quantum-projects/issues",
    },
)