from setuptools import find_packages, setup
from pathlib import Path

# Load long description from README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="pyzmap",
    version="0.1.1",
    description="Python SDK for the ZMap network scanner with REST API support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Atilla",
    author_email="attilla@tuta.io",
    url="https://github.com/atiilla/pyzmap",
    packages=find_packages(),
    install_requires=[
        "pydantic>=1.8.0,<2.0.0",    # Data validation
        "fastapi>=0.68.0",           # REST API
        "uvicorn>=0.15.0",           # ASGI server
        "psutil>=5.8.0",             # System/process monitoring
        "httpx>=0.18.0",             # HTTP client
        "click>=8.1.8,<9.0.0",       # CLI
        "tomli>=2.0.1,<3.0.0",       # TOML reader
        "tomlkit>=0.13.2,<0.14.0",   # TOML writer/editor
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
