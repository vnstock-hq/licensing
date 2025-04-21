from setuptools import setup, find_packages

setup(
    name="vnii",
    version="0.0.8",
    author="Vnstock HQ",
    author_email="support@vnstocks.com",
    description="",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=["requests", "cryptography"],
    extras_require={"dev": ["pytest", "pytest-cov"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
