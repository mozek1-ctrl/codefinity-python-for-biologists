import matplotlib.pyplot as plt

def plot_gc_content(sequences):
    # Write your code here
    gc_contents = []
    for seq in sequences:
        count = sum(1 for b in seq.upper() if b in ("G", "C"))
        gc_contents.append((count/len(seq)) * 100 if seq else 0)

    color_list = ["red" if gc >60 else "blue" for gc in gc_contents]

    idx = list(range(len(sequences)))
    plt.bar(idx, gc_contents, color=color_list)
    plt.xticks(idx, [str(i) for i in idx])
    plt.xlabel("Sequence Index")
    plt.ylabel("GC Content (%)")
    plt.title("GC content of DNA sequences")
    plt.ylim(0, 100)

    plt.show()
sequences = [
    "ATGCGCGTA",
    "ATATATATAT",
    "GGGCCCGGG",
    "TTAACCGGTT",
    "GCGCGCGCGC"
]
plot_gc_content(sequences)
