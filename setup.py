## 📁 **File 4: `setup.py` (place in root directory)**

```python
#!/usr/bin/env python3
"""
Setup script for Prework Study Guide
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="prework-study-guide",
    version="1.0.0",
    author="Justin D.",
    author_email="lacespidermath@gmail.com",
    description="A beautiful CLI quiz tool for programming fundamentals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Myrmecology/prework-study-guide",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: Software Development",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "study-quiz=quiz_app:main",
        ],
    },
    keywords="quiz, study, programming, interview, education, cli, python",
    project_urls={
        "Bug Reports": "https://github.com/Myrmecology/prework-study-guide",
        "Source": "https://github.com/Myrmecology/prework-study-guide",
    },
)