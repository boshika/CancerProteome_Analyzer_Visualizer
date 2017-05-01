# Cancer Proteome: Analyzer and Visualizer

1. [Abstract](#abstract)
1. [Requirements](#requirements)
1. [Development](#development)
    1. [Installation](#installation)
    2. [Running the program](#running-program)
    3. [Documentation](#documentation)
1. [Run-time Graphs](#graphs)
1. [Team](#team)

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
