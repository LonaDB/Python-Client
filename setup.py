from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="lonadb-client",
    version="1.2",
    author="Collin Buchkamer",
    author_email="collin@kisara.app",
    description="A client library for interacting with LonaDB server",
    url="https://github.com/LonaDB/Python-Client",
    packages=["lonadb_client"],
    install_requires=[
        "pycryptodome"
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
