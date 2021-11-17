# remove chimeras, look for lines that start with the chimera (read in from chim list) a
# only write lines which do not have chimeras

#reading in chimeras

from Bio import SeqIO
chimList =[]
fasta_sequences = SeqIO.parse(open('C:/Users/jjcol/Downloads/chimeraList.fa'),'fasta')
for fasta in fasta_sequences:
    chimList.append(str(fasta.seq))

#reading in table
seqtab= open("C:/Users/jjcol/Downloads/seqtabTransposed.txt", "r")
seqtab.nochim =[] 
counter = 0 

for line in seqtab:
    counter +=1 
    isIn = False
    for chim in chimList:
        if line.startswith(chim)== True:
            isIn = True
    if isIn == False:
        seqtab.nochim.append(line)
output = open('C:/Users/jjcol/Downloads/seqtab.nochimTransposed.txt','w')

for s in seqtab.nochim:
    output.write(s)
output.close()
