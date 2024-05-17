rna='AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'


amino_acids={'AUG':'M','UUU':'F','UUC':'F','UUA':'L','UUG':'L','UCU':'S',
                 'UCC':'S','UCA':'S','UCG':'S','CUU': 'L','AUU': 'I','GUU': 'V',
                 'CUC': 'L','AUC': 'I','GUC': 'V','CUA': 'L','AUA': 'I','GUA': 'V',
                 'CUG': 'L','GUG': 'V','CCU': 'P', 'ACU': 'T','GCU': 'A','CCC': 'P',
                 'ACC': 'T','GCC': 'A','CCA': 'P','ACA': 'T','GCA': 'A','CCG': 'P',
                 'ACG': 'T','GCG': 'A','UAU': 'Y','CAU': 'H','AAU': 'N','GAU': 'D',
                 'UAC': 'Y','CAC': 'H','AAC': 'N','GAC': 'D','UAA': '*','CAA': 'Q',
                 'AAA': 'K','GAA': 'E','UAG': '*','CAG': 'Q','AAG': 'K','GAG': 'E',
                 'UGU': 'C','CGU': 'R','AGU': 'S','GGU': 'G','UGC': 'C','CGC': 'R',
                 'AGC': 'S','GGC': 'G','UGA': '*','CGA': 'R','AGA': 'R','GGA': 'G',
                 'UGG': 'W','CGG': 'R','AGG': 'R','GGG': 'G'}
rna=list(rna)
#print(rna)
liste=''
for i in range(0,len(rna)-2,3):
    combined= rna[i]+rna[i+1]+rna[i+2]
    
    for j in range(0, len(amino_acids.items())):
        
        if combined == list(amino_acids.keys())[j]:
           key=amino_acids.get(combined)
           if key!='*':
              liste+=key  
              print(liste)
           else: 
              break
                   
                   