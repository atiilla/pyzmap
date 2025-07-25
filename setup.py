from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyzmap",
    version="0.1.0",
    description="Python SDK for the ZMap network scanner with REST API",
    author="Atilla",
    author_email="attilla@tuta.io",
    url="https://github.com/atiilla/pyzmap",
    packages=find_packages(),
    install_requires=[
        "pydantic>=1.8.0,<2.0.0",  # For data validation
        "fastapi>=0.68.0",  # For REST API
        "uvicorn>=0.15.0",  # For serving the API
        "psutil>=5.8.0",  # For system and process management
        "httpx>=0.18.0",  # For making HTTP requests
        "click>=8.1.8,<9.0.0",  # CLI support
        "tomli>=2.0.1,<3.0.0",  # TOML parsing
        "tomlkit>=0.13.2,<0.14.0",  # TOML editing
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "black>=21.5b2",
            "isort>=5.9.1",
            "mypy>=0.812",
        ],
    },
    entry_points={
        "console_scripts": [
            "pyzmap=pyzmap.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet",
        "Topic :: Security",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.7",
)
