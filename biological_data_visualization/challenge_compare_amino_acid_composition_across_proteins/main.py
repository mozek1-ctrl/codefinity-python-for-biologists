import matplotlib.pyplot as plt

def plot_amino_acid_compositions(sequences, protein_labels=None):
    # Write your code here
    pass
    amino_acids = [
        'A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'
        ]

#computation of the amount of amino acids within the sequence

    compositions = []
    for seq in sequences:
        seq = seq.upper()
        length = len(seq)
        comp = []
        for aa in amino_acids:
            count = seq.count(aa)
            comp.append(count / length if length >0 else 0)
        compositions.append(comp)

    num = len(sequences)
    if protein_labels is None or len(protein_labels) != num:
        protein_labels = [f"Protein {i+1}" for i in range(num)]

    #plotting of data
    bar_width = 0.8 / num
    x = range(len(amino_acids))
    plt.figure(figsize=(12,6))
    for i, comp in enumerate(compositions):
        positions = [xi + i * bar_width for xi in x]
        plt.bar(positions, comp, width=bar_width, label=protein_labels[i])
    plt.xticks([xi + bar_width*(num-1)/2 for xi in x], amino_acids)
    plt.xlabel("Amino Acids")
    plt.ylabel("Frequency of Amino Acid in Sequence")
    plt.title("Amino Acid Frequency within Protein Sequence Composition")
    plt.legend()
    plt.tight_layout()
    plt.show()
    

# Sample calls
sequences = [
    "MKTFFVAGVILLLPLVSSQCVNLTTRTQ",
    "MGLSDGEWQLVLNVWGKVEADIPGHGQEVLIRLFKG",
    "MKKFFDSRREQMKLQK"
]
protein_labels = ["Sample1", "Sample2", "Sample3"]
plot_amino_acid_compositions(sequences, protein_labels)
