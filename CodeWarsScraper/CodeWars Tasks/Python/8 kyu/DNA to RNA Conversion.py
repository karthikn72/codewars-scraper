def DNAtoRNA(dna):
    rna=dna
    for i in range(len(dna)):
      if dna[i]=="T":
        rna=rna[:i]+"U"+rna[i+1:]
    return rna


    # create a function which returns an RNA sequence from the given DNA sequence