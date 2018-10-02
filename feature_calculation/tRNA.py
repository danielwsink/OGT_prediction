import logging
logger = logging.getLogger('feature_calculation')

def analysis(data):
	#calculate all features of the tRNA sequences
	results ={}
	results['Nucleotide Fraction']=nucleotide_freq(data)
	results['GC']=GC(data)
	results2 = {}
	for key in results.keys():
		if isinstance(results[key],dict):
			for subkey in results[key].keys():
				results2[key+': '+subkey]=results[key][subkey]
		else: 
			results2[key] = results[key]
	return results2

def GC(data):
	#calculate the GC fraction of the tRNA sequences
	#ignore Ns
	A=0.0
	G=0.0
	T=0.0
	C=0.0
	for x in data:
		input_seq = data[x]
		input_seq = input_seq.seq
		A = A+float(input_seq.count('A'))
		G = G+float(input_seq.count('G'))
		T = T+float(input_seq.count('T'))
		C = C+float(input_seq.count('C'))
	total = A+G+T+C
	return (G+C)/total
	
def nucleotide_freq(data):
	#calculate the nucleotide fraction of the tRNA sequences
	#ignore Ns
	#as this is read from the genome, count T's rather than U's
	A=0.0
	G=0.0
	T=0.0
	C=0.0
	for x in data:
		input_seq = data[x]
		input_seq = input_seq.seq
		A = A+float(input_seq.count('A'))
		G = G+float(input_seq.count('G'))
		T = T+float(input_seq.count('T'))
		C = C+float(input_seq.count('C'))
	total = A+G+T+C
	return {'A':A/total,'C':C/total,'G':G/total,'T':T/total}
