def to_rna(dna_strand):
    mapping = {
        'A':'U',
        'G':'C',
        'C':'G',
        'T':'A'
    }
    rna =''
    for base in dna_strand:
        rna +=mapping[base]
    return rna
