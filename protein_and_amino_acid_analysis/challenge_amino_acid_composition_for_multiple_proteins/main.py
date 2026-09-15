def amino_acid_compositions(sequences):
    # Write your code here
    valid_aa = set("ACDEFGHIKLMNPQRSTVWY")
    compositions = []
    for seq in sequences:
        seq = seq.upper()
        aa_counts = {}
        total_valid = 0
        for aa in seq:
            if aa in valid_aa:
                aa_counts[aa] = aa_counts.get(aa, 0) + 1
                total_valid += 1
        if total_valid == 0:
            compositions.append({})
            continue
        comp_dict = {}
        for aa, count in aa_counts.items():
            comp_dict[aa] = (count / total_valid) * 100
        compositions.append(comp_dict)
    return compositions 
# Sample calls
seqs = [
    "MKTIIALSYIFCLVFADYKDDDDA",
    "GAVLIPFYWSTCMNQDEKRH",
    "MXXKZZ",
    ""
]
result = amino_acid_compositions(seqs)
print(result)
