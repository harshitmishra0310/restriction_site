# 🧬 DNA Restriction Site Finder

A Python-based bioinformatics tool that identifies restriction enzyme recognition sites within DNA sequences and predicts their cleavage locations. The program scans DNA for **30+ commonly used restriction enzymes**, detects multiple recognition sites, and simulates where each enzyme cuts the DNA.

This project demonstrates one of the fundamental techniques in molecular biology and genetic engineering by implementing the core logic behind restriction enzyme analysis from scratch.

---

# 📸 Screenshots

### 🔍 Restriction Site Detection

![img alt](https://github.com/harshitmishra0310/restriction_site/blob/a5b6bd5dee7eb91cac21fe60a36437243cc316af/Working.png)

---

# ✨ Features

* 🧬 Validates DNA sequences before analysis
* 🔍 Detects **30+ common restriction enzyme recognition sites**
* 🔄 Identifies multiple occurrences of the same restriction site
* ✂️ Predicts enzyme-specific DNA cleavage locations
* 🧪 Simulates DNA digestion by displaying cut positions
* 📏 Displays DNA sequence length
* 📊 Presents results in a clean, organized console format
* 🗂 Easily expandable restriction enzyme database

---

# 🧠 Biological Workflow

```text
DNA Sequence

│

▼

Sequence Validation

│

▼

Restriction Enzyme Database

│

▼

Recognition Site Search

│

▼

Restriction Site Detection

│

▼

Cleavage Position Prediction

│

▼

DNA Digestion Simulation
```

---

# 🧬 Restriction Enzymes Included

The program currently supports **30 commonly used restriction enzymes**, including:

| Enzyme  | Recognition Sequence |
| ------- | -------------------- |
| EcoRI   | GAATTC               |
| BamHI   | GGATCC               |
| HindIII | AAGCTT               |
| NotI    | GCGGCCGC             |
| PstI    | CTGCAG               |
| XhoI    | CTCGAG               |
| SalI    | GTCGAC               |
| KpnI    | GGTACC               |
| NheI    | GCTAGC               |
| SpeI    | ACTAGT               |
| XbaI    | TCTAGA               |
| ApaI    | GGGCCC               |
| SmaI    | CCCGGG               |
| SacI    | GAGCTC               |
| SacII   | CCGCGG               |
| EagI    | CGGCCG               |
| BglII   | AGATCT               |
| ClaI    | ATCGAT               |
| NcoI    | CCATGG               |
| NdeI    | CATATG               |
| MluI    | ACGCGT               |
| AvrII   | CCTAGG               |
| AflII   | CTTAAG               |
| SphI    | GCATGC               |
| AgeI    | ACCGGT               |
| BspHI   | TCATGA               |
| BclI    | TGATCA               |
| StuI    | AGGCCT               |
| PvuII   | CAGCTG               |
| HaeIII  | GGCC                 |

---

# 🧪 Example Run

### Input

```text
Enter a DNA sequence:

ATGAATTCGGATCCAAGCTTGCGGCCGCCTGCAG
```

### Output

```text
============================================================
               DNA RESTRICTION SITE FINDER
============================================================

✓ DNA sequence is valid.

------------------------------------------------------------
GENERAL INFORMATION
------------------------------------------------------------

Sequence Length : 34 bp

------------------------------------------------------------
RESTRICTION SITE ANALYSIS
------------------------------------------------------------

Enzyme             : EcoRI
Recognition Site   : GAATTC
Position           : 3
Cut Position       : 3
Digested Sequence  : ATG|AATTCGGATCCAAGCTTGCGGCCGCCTGCAG

Enzyme             : BamHI
Recognition Site   : GGATCC
Position           : 9
Cut Position       : 9
Digested Sequence  : ATGAATTCG|GATCCAAGCTTGCGGCCGCCTGCAG

Enzyme             : HindIII
Recognition Site   : AAGCTT
Position           : 15
Cut Position       : 15
Digested Sequence  : ATGAATTCGGATCCA|AGCTTGCGGCCGCCTGCAG
```

---

# 🔬 Understanding the Results

* **Sequence Length** displays the total number of nucleotides in the DNA sequence.
* **Recognition Site** identifies the specific DNA sequence recognized by a restriction enzyme.
* **Position** indicates where the recognition sequence begins within the DNA.
* **Cut Position** predicts where the enzyme cleaves the DNA strand.
* **Digested Sequence** visually represents the DNA with the cleavage site marked using the `|` symbol.

---

# 🧬 How Restriction Enzymes Work

Restriction enzymes recognize specific DNA sequences and cut the DNA at defined positions.

### Example

```text
Recognition Sequence

GAATTC

↓

EcoRI Cleavage

G|AATTC
```

After cleavage:

```text
ATCGAATTCGG

↓

ATCG|AATTCGG
```

This process forms the basis of molecular cloning, recombinant DNA technology, plasmid construction, genome engineering, and many DNA sequencing workflows.

---

# ⚙️ Technologies Used

* 🐍 Python 3
* 🧬 Bioinformatics algorithms
* 🔁 String searching
* 📚 Dictionaries & tuples
* 🔄 Loops and conditional statements
* 🧪 Restriction enzyme analysis
* 🧬 DNA sequence validation

---

# 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/dna-restriction-site-finder.git
```

### 2. Navigate to the project folder

```bash
cd dna-restriction-site-finder
```

### 3. Run the program

```bash
python restriction_site_finder.py
```

### 4. Enter a DNA sequence when prompted.

---

# 📚 Scientific Concepts Demonstrated

* DNA sequence validation
* Restriction enzymes
* Restriction endonucleases
* DNA cleavage prediction
* Pattern matching in biological sequences
* Recognition sequence analysis
* Multiple restriction site detection
* Molecular cloning fundamentals
* Computational biology algorithms

---

# 🎯 Learning Outcomes

This project helped strengthen my understanding of:

* Python programming and algorithm design
* Biological sequence analysis
* Restriction enzyme recognition mechanisms
* DNA cleavage simulation
* Pattern searching in genomic sequences
* Practical applications of computational biology
* Software development for bioinformatics

---

# 🚀 Future Improvements

* 📂 FASTA file support
* 📊 CSV export of restriction site data
* 📏 DNA fragment size calculation
* 🧬 IUPAC ambiguity code support
* 🗺 Restriction map visualization
* 🧪 Biopython integration
* 🖥 Graphical User Interface (GUI)

---

# 👨‍💻 Author

**Harshit Mishra**

Aspiring Bioinformatics student passionate about computational biology, genomics, biotechnology, and applying programming to solve biological problems.

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ If you found this project useful or interesting, consider giving the repository a star and following my journey into bioinformatics and computational biology!
