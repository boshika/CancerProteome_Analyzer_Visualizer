#!/usr/bin/python3


from collections import defaultdict
import requests
from Bio import ExPASy, SwissProt
import pandas as pd
import StringIO
import mysqlconnector


server = 'http://www.uniprot.org/uniprot'


def do_request(server, ID='', **kwargs):
    # type: (object, object, object) -> object

    params = ''
    req = requests.get('%s/%s%s' % (server, ID, params), params=kwargs)
    if not req.ok:
        req.raise_for_status()
    return req

#Method for extracting features for each protein including Gene Ontology
def extract_features(protein):
    done_features = set()
    print(len(protein.features))
    for feature in protein.features:
        if feature[0] in done_features:
            continue
        else:
            done_features.add(feature[0])
            print(feature)
    print(len(protein.cross_references))
    per_source = defaultdict(list)
    for xref in protein.cross_references:
        source = xref[0]
        per_source[source].append(xref[1:])
    print(per_source.keys())
    done_GOs = set()
    print(len(per_source['GO']))
    for annot in per_source['GO']:
        if annot[1][0] in done_GOs:
            continue
        else:
            done_GOs.add(annot[1][0])
            print(annot)


#p53
req = do_request(server, query='gene:p53 AND reviewed:yes AND organism:Human',
                 format='tab',
                 columns='entry name,length,organism,organism-id,database(PDB),database(HGNC)'
                 )

uniprot_list = pd.read_table(StringIO.StringIO(req.text))
uniprot_list.rename(columns={'Organism ID': 'ID'}, inplace=True)
print(uniprot_list)

# print(uniprot_list.iloc[:,[0]])
# print(uniprot_list.iloc[:,[1]])
# print(uniprot_list.iloc[:,[3]])

#additional features

p53_human = uniprot_list[uniprot_list.ID == 9606]['Entry name'].tolist()[0]
handle = ExPASy.get_sprot_raw(p53_human)
sp_rec = SwissProt.read(handle)

# print(sp_rec.entry_name, sp_rec.sequence_length, sp_rec.gene_name)
# print(sp_rec.description)
# print(sp_rec.organism, sp_rec.seqinfo)
# print(sp_rec.sequence)


# extract_features(sp_rec)


#myc
req = do_request(server, query='gene:myc AND reviewed:yes AND organism:Human',
                 format='tab',
                 columns='entry name,length,organism,organism-id,database(PDB),database(HGNC)'
                 )

uniprot_list1 = pd.read_table(StringIO.StringIO(req.text))
uniprot_list1.rename(columns={'Organism ID': 'ID'}, inplace=True)
print(uniprot_list1)

# print(uniprot_list1.iloc[:,[0]])
# print(uniprot_list1.iloc[:,[1]])
# print(uniprot_list1.iloc[:,[3]])

#additional myc analysis
myc = uniprot_list1[uniprot_list1.ID == 9606]['Entry name'].tolist()[0]
handle1 = ExPASy.get_sprot_raw(myc)
sp_rec1 = SwissProt.read(handle1)

# print(sp_rec1.entry_name, sp_rec.sequence_length, sp_rec.gene_name)
# print(sp_rec1.description)
# print(sp_rec1.organism, sp_rec.seqinfo)
# print(sp_rec1.sequence)

extract_features(sp_rec1)


#errb2
req = do_request(server, query='gene:her2 AND reviewed:yes AND organism:Human',
                 format='tab',
                 columns='entry name,length,organism,organism-id,database(PDB),database(HGNC)'
                 )

uniprot_list2 = pd.read_table(StringIO.StringIO(req.text))
uniprot_list2.rename(columns={'Organism ID': 'ID'}, inplace=True)
print(uniprot_list2)

# print(uniprot_list2.iloc[:,[0]])
# print(uniprot_list2.iloc[:,[1]])
# print(uniprot_list2.iloc[:,[3]])

#additional errb2 analysis
errb2 = uniprot_list2[uniprot_list2.ID == 9606]['Entry name'].tolist()[0]
handle2 = ExPASy.get_sprot_raw(errb2)
sp_rec2 = SwissProt.read(handle2)

# print(sp_rec2.entry_name, sp_rec2.sequence_length, sp_rec2.gene_name)
# print(sp_rec2.description)
# print(sp_rec2.organism, sp_rec2.seqinfo)
# print(sp_rec2.sequence)


# extract_features(sp_rec2)


#Epidermal Growth Factor
req = do_request(server, query='gene:egfr AND reviewed:yes AND organism:Human',
                 format='tab',
                 columns='entry name,length,organism,organism-id,database(PDB),database(HGNC)'
                 )

uniprot_list3 = pd.read_table(StringIO.StringIO(req.text))
uniprot_list3.rename(columns={'Organism ID': 'ID'}, inplace=True)
print(uniprot_list3)

# print(uniprot_list3.iloc[:,[0]])
# print(uniprot_list3.iloc[:,[1]])
# print(uniprot_list3.iloc[:,[3]])

#additional egfr analysis
egfr = uniprot_list3[uniprot_list3.ID == 9606]['Entry name'].tolist()[0]
handle3 = ExPASy.get_sprot_raw(egfr)
sp_rec3 = SwissProt.read(handle3)

# print(sp_rec3.entry_name, sp_rec3.sequence_length, sp_rec3.gene_name)
# print(sp_rec3.description)
# print(sp_rec3.organism, sp_rec3.seqinfo)
# print(sp_rec3.sequence)


# extract_features(sp_rec3)

#Pten
req = do_request(server, query='gene:pten AND reviewed:yes AND organism:Human',
                 format='tab',
                 columns='entry name,length,organism,organism-id,database(PDB),database(HGNC)'
                 )

uniprot_list4 = pd.read_table(StringIO.StringIO(req.text))
uniprot_list4.rename(columns={'Organism ID': 'ID'}, inplace=True)
print(uniprot_list4)

# print(uniprot_list4.iloc[:,[0]])
# print(uniprot_list4.iloc[:,[1]])
# print(uniprot_list4.iloc[:,[3]])

#additional pten analysis
pten = uniprot_list4[uniprot_list4.ID == 9606]['Entry name'].tolist()[0]
handle4 = ExPASy.get_sprot_raw(pten)
sp_rec4 = SwissProt.read(handle4)

# print(sp_rec4.entry_name, sp_rec4.sequence_length, sp_rec4.gene_name)
# print(sp_rec4.description)
# print(sp_rec4.organism, sp_rec4.seqinfo)
# print(sp_rec4.sequence)

extract_features(sp_rec4)




#PUSH DATA TO THE DATABASE
cursor = mysqlconnector.conn.cursor()
#
# should be done using a better way, extracting data from uniprot API and hardcoding it defeats the purpose
data = [
        (1,'P53', 393, sp_rec.description, "GO:0000785, C:chromatin, IBA:GO_Central GO:0005524, F:ATP binding, \
                                            IDA:UniProtKB GO:0006915, \
                                            P:apoptotic process, TAS:Reactome"),
        (2,'MYC', 439, sp_rec2.description, "GO:0005829, C:cytosol, TAS:Reactome \
                                             GO:0003677, F:DNA binding, ISS:UniProtKB) \
                                             GO:1904837, P:beta-catenin-TCF complex assembly, TAS:Reactome"),
        (3,'ERRB2',1255, sp_rec2.description, "GO:0016324, C:apical plasma membrane, IEA:Ensembl \
                                               GO:0005524, F:ATP binding', IEA:UniProtKB-KW \
                                               GO:0008283, P:cell proliferation, TAS:ProtInc"),
        (4,'EGFR', 1210,  sp_rec3.description, "GO:0009897, C:external side of plasma membrane, IDA:MGI \
                                                GO:0030246, F:carbohydrate binding', 'IEA:UniProtKB-KW"),
        (5,'PTEN', 403, sp_rec4.description, "GO:0016324, C:apical plasma membrane, IMP:UniProtKB \
                                              GO:0010997', F:anaphase-promoting complex binding, IPI:BHF-UCL \
                                              GO:0030534, P:adult behavior, IEA:Ensembl")
        ]
cursor.executemany("""INSERT INTO cancer VALUES (%s,%s,%s,%s,%s)""", data)
mysqlconnector.conn.commit()
