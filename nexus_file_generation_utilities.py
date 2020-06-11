#Depends on Biopython
from Bio import SeqIO

def create_matrix_string(taxa_list):
    s = ""
    for sequence in taxa_list:
        s += ("\t{}\t{}\n".format(sequence.id,sequence.seq))
    return s


def create_method_string(method):
    if method == "nj":
        method_string = "set criterion = distance;\nnj brlens = yes treefile=njtree.tre;"
    elif method == "mp":
        method_string = "set criterion = parsimony;\nhsearch addseq=random nreps=1000;"
    else:
        raise ValueError("The PAUP* method is not known. Only MP and NJ are supported")
    return method_string

def create_nexus_file(taxa_list,out_filename,method):
    for i in range(len(taxa_list)):
        if len(taxa_list[i]) != len(taxa_list[i-1]):
            raise ValueError("the sequences do not have equal length!")
    
    template ="""#NEXUS
Begin data;
  dimensions ntax={num_taxa} nchar={seq_len};
  format datatype=protein missing=? gap=-;
  matrix
{matrix}
    ;
end;

Begin Paup;
{method_string}
savetrees /file={filename} format=newick
;

end;
""".format(num_taxa = len(taxa_list),seq_len=len(taxa_list[0]),matrix = create_matrix_string(taxa_list),filename=out_filename,method_string = create_method_string(method))

    return template



def nexus_from_fasta(fasta_path,method = "nj"):
    taxa = []
    out_path = fasta_path.replace(".fasta",".paup.treefile")
    for seq_record in SeqIO.parse(fasta_path, "fasta"):
        taxa.append(seq_record)
    
    fasta_template = create_nexus_file(taxa,out_path,method)
    return fasta_template
