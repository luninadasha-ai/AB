def seq_identity(seq1, seq2):
    """
    Return the percentage of sequence identity. Exclude positions with gaps on any sequence
    >>> seq_identity("FASTCAT", "FATCAT")

    >>> seq_identity("FASTCAT", "FASTCAT")
    100.0
    >>> seq_identity("FASTCAT", "FASTRAT")
    85.7
    >>> seq_identity("-FASTCAT", "-FASTRAT")
    85.7
    >>> seq_identity("FASTCAT", "FA-TCAT")
    100.0
    >>> seq_identity("FASTCAT", "FAT-CAT")
    83.3
    >>> seq_identity("AFASTCAT", "-FASTRAT")
    85.7
    >>> seq_identity("FASTCAT", "AAAAAAA")
    28.6
    >>> seq_identity("FASTCAT", "AFAAAFA")
    0.0
    """
    # YOUR CODE HERE
    if len(seq_1) != len(seq_2):
        return
    position = 0
    match = 0

    for a,b in zip(seq_1, seq_2):
        if a == "-" or b == "-":
            continue
        else:
            position += 1
            if a == b:
                match += 1
    if position == 0:
        return 0.0
    
    percentage = (match/position) * 100
    return round(percentage, 1)
