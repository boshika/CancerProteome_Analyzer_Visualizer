# Cancer Proteome: Analyzer and Visualizer

1. [Abstract](#abstract)
1. [Requirements](#requirements)
1. [Development](#development)
    1. [Installation](#installation)
    2. [Running the program](#running-program)
    3. [Documentation](#documentation)

## Abstract
Proteomics is the study of protein that includes protein function and structure. One of the main objectives of this field is to explore the 3D structure of proteins. This application utilizes the main objective of proteomics. The user can explore a specific set of genes involved in cancer.  It allows users to access information about that specific biomolecule, and run basic analysis and visualize its models.

Specific Objectives
-   Users can access pre-populated data such as features, gene ontology, cross-references on certain genes that are involved in cancer
-   User can select certain aspects of the protein to explore, such as looking at spatial distribution of the protein chains, a basic computation of the molecular distances, and 3D structure of the protein

## Requirements
- [Python](https://www.python.org/download/releases)
- [BioPython](http://biopython.org//wiki/Biopython)
- [UniProt REST API](http://www.uniprot.org/help/programmatic_access)
- [Requests library](http://docs.python-requests.org/en/master/)
- [Pandas](http://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [PyMol](https://www.pymol.org/)
- [D3.js](https://d3js.org/)

## Development

### Installation

The user can access limited about of protein data via a web page at Cancer Proteomics: Visualizer and Analyzer, this will allow users to see pre-populated data for a limited set of proteins. There is a drop-down menu, from where a user can choose the protein of interest.

Alternately, if the user is interested in a protein that is not listed on the web page, they can set the project locally by following these steps 
```
    Fork and clone the CancerProteome_Analyzer_Visualizer Repository from GitHub`
```
To import the database
```sql
    $ mysql –u <yourusername> -p <yourpassword> -h localhost proteomics < proteomics.sql
```
Install Dependencies using HomeBrew(if on Windows use pip for all these packages)
```
    $ brew update
    $ brew install Python
    $ brew install mysql
    $ brew tap homebrew/science
    $ brew install matpoltlib

    Pandas, Requests and BioPython should install via pip:
    $ pip install pandas
    $ pip install biopython
    $ pip install requests
```
Server set-up to run CGI scripts(there are a lot of ways to do this)
```
    $ brew install node
    $ npm install http-server –g
```
To start the server type
```
    $ http-server
```
You should see the port at which the page is available, for me it was Port 8080. Open the page at
```
    localhost:8080
```
Another alternate is using either a server like Apache or WebBricks

### Running-program

There are two file in the directory that can be used for analysis uniprot.py and pdb.py.

#### Sample Analysis using UniProt Script(uniprot.py)
In the project directory
```python
    $ python
>>> import uniprot
>>> import requests
>>> import pandas as pd
>>> req(uniprot.server,  query=’gene:<protein name> AND organism: Human’ AND reviewed:yes’)
>>> uniprot_list = pd.read_table(StringIO.StringIO(req.text))
>>> uniprot_list.rename(columns={]Organism IS: ‘ID’}, inplace=True)
>>> <protein name> = uniprot_list[uniprot.list.ID == 9606][‘Entry Name’].tolist()[0]
>>> handle = ExPASy.getsprot_raw(<protein name>)
>>> sp_rec = SwissProt.read(handle)
>>> uniprot.extract_features(sp_rec)
```
#### Sample Analysis of a model for above protein using BioPython PDB(pdb.py)
In the project directory

```python
    $ python
>>> from Bio import PDB
>>> from Bio.PDB import *
>>> import matplotliv.pyplot as plt
>>> repository = PDB.PDBList()
>>> parser = MMCIFParser()
>>> repository.retrieve_pdbfile(<model_of_choice>)
>>> <model name> = parser.get_structure(‘name’, <protein_model.cif>)
>>> pdb.describe_model(<name, <model name>)
>>> pdb.plot(<model name>)
```
**Note: A protein can have many models, with many different configurations, this program 
and some of its methods are not generic methods. You might have to configure the methods to your model of choice e.g. looking for residues in a chain.**

Alternate would be to configure these scripts according to your protein model of choice. Added benefit of this is you will be able to save this data to the proteomics database. For that add too data and pdb_data lists.


