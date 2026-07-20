"""
DNA Restriction Site Finder

Analyzes a DNA sequence to identify restriction enzyme recognition sites
and predict cleavage locations.

Features:
• DNA sequence validation
• Detection of restriction enzyme recognition sites
• Multiple occurrence detection
• Cleavage site simulation
• Easy-to-expand enzyme database

Restriction enzymes included:
• EcoRI
• BamHI
• HindIII
• NotI
• PstI
"""

print("=" * 60)
print("               DNA RESTRICTION SITE FINDER")
print("=" * 60)

# ==========================================================
# DNA INPUT & VALIDATION
# ==========================================================

dna = input("\nEnter a DNA sequence: ").upper().strip()

if len(dna) == 0:
    print("\n✗ DNA sequence cannot be empty.")
    exit()

for base in dna:
    if base not in "ATGC":
        print("\n✗ DNA sequence is invalid.")
        exit()

print("\n✓ DNA sequence is valid.")

# ==========================================================
# GENERAL INFORMATION
# ==========================================================

print("\n" + "-" * 60)
print("GENERAL INFORMATION")
print("-" * 60)

print(f"Sequence Length : {len(dna)} bp")

# ==========================================================
# RESTRICTION ENZYME DATABASE
# (Recognition Sequence, Cut Offset)
# ==========================================================

restriction_enzymes = {
    "EcoRI": ("GAATTC", 1),
    "BamHI": ("GGATCC", 1),
    "HindIII": ("AAGCTT", 1),
    "NotI": ("GCGGCCGC", 2),
    "PstI": ("CTGCAG", 5),
    "XhoI": ("CTCGAG", 1),
    "SalI": ("GTCGAC", 1),
    "KpnI": ("GGTACC", 5),
    "NheI": ("GCTAGC", 1),
    "SpeI": ("ACTAGT", 1),
    "XbaI": ("TCTAGA", 1),
    "ApaI": ("GGGCCC", 5),
    "SmaI": ("CCCGGG", 3),
    "SacI": ("GAGCTC", 5),
    "SacII": ("CCGCGG", 2),
    "EagI": ("CGGCCG", 1),
    "BglII": ("AGATCT", 1),
    "ClaI": ("ATCGAT", 2),
    "NcoI": ("CCATGG", 1),
    "NdeI": ("CATATG", 2),
    "MluI": ("ACGCGT", 1),
    "AvrII": ("CCTAGG", 1),
    "AflII": ("CTTAAG", 1),
    "SphI": ("GCATGC", 5),
    "AgeI": ("ACCGGT", 1),
    "BspHI": ("TCATGA", 1),
    "BclI": ("TGATCA", 1),
    "StuI": ("AGGCCT", 3),
    "PvuII": ("CAGCTG", 3),
    "HaeIII": ("GGCC", 2)
}

# ==========================================================
# RESTRICTION SITE ANALYSIS
# ==========================================================

print("\n" + "-" * 60)
print("RESTRICTION SITE ANALYSIS")
print("-" * 60)

found = False

for enzyme, (site, cut_offset) in restriction_enzymes.items():

    positions = []
    start = 0

    while True:

        position = dna.find(site, start)

        if position == -1:
            break

        positions.append(position + 1)

        cut_position = position + cut_offset

        cut_dna = dna[:cut_position] + "|" + dna[cut_position:]

        print(f"\nEnzyme             : {enzyme}")
        print(f"Recognition Site   : {site}")
        print(f"Position           : {position + 1}")
        print(f"Cut Position       : {cut_position}")
        print(f"Digested Sequence  : {cut_dna}")

        start = position + 1
        found = True

if not found:
    print("\nNo restriction sites found.")

print("\n" + "=" * 60)
print("      RESTRICTION SITE ANALYSIS COMPLETED")
print("=" * 60)