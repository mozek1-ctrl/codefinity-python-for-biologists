#Scatterplotting of protein GC content
 
import matplotlib.pyplot as plt

sequences = [
    "ATGCGCGTAC",
    "ATATATATATAT",
    "CGCGCGCGCGCGCGCGCGCG",
    "ATGC",
    "GGGGGGGGGGGGGG",
    "TATATATATATA",
    "ATGCGC",
    "ATATATAT",
    "GCGCGCGCGCGC",
    "ATGCGTACGTAGCTAGCTAGCTAGCTAGCTA"
]

groups = ["A", "A", "B", "A", "B", "A", "A", "A", "B", "B"]

def calculate_gc_content(seq):
    seq = seq.upper()
    gc_count = seq.count("G") + seq.count("C")
    return (gc_count / len(seq)) * 100 if len(seq) > 0 else 0

def plot_length_gc(sequences, groups=None):
    lengths = [len(seq) for seq in sequences]
    gc_contents = [gc_content_calculate(seq) for seq in sequences]

    #Function to detect and mark the outliers with an interqauter range of 1.5
    import numpy as np 
    def outlier_indices(data):
        q1 = np.percentile(data, 25)
        q3 = np.percentile(data, 75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        return [i for i, val in enumerate(data) if val < lower or val > upper]

    outlier_index = set(outlier_indices(lengths) + outlier_indices(gc_contents))

    # Colour Coding

    if groups is not None:
        unique_groups = list(dict.fromkeys(groups))
        colour_map = {g: plt.cm.tab10(i % 10) for i, g in enumerate(unique_groups)}
        colors = [colour_map[g] for g in groups]
    else:
        colors = "blue"

    fig, ax = plt.subplots()
    scatter = ax.scatter(lengths, gc_contents, c=colors, edgecolors="k", alpha=0.8)

    ax.set_xlabel("Sequence Length")
    ax.set_ylabel("GC Content %")
    ax.set_title("Sequence Length vs GC Content %")

    if groups is not None:
        handles = [
            plt.Line2D([0],[0], marker='o', color='w', label=g,
                       markerfacecolor=colour_map[g], markersize=8, markeredgecolor='k')
                       for g in unique_groups
        ]
        ax.legend(handles=handles, title="Groups")

    plt.tight_layout()
    plt.show()



plot_length_gc(sequences, groups)