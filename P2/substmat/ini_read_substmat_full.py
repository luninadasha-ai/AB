def read_substmat_full(filename):
    """Reads a substitution matrix from a file."""
    # YOUR CODE HERE
    substmat = {}
    try: 
        with open (file_name, "rt") as fn:
                aminos_1 = fn.readline()
                aminos_1 = aminos_1.strip().split()
                for letter in aminos_1:
                     for l in fn:
                            l = fn.readline()
                            l = l.strip().split()
                            substmat[letter] = l[0]
                            substmat[letter][l[0]] = l[aminos_1.index(letter)+1]
        return substmat
    except FileNotFoundError:
        print("File not found.")

    except PermissionError:
        print("Permission denied.")

    except UnicodeDecodeError:
        print("Encoding error while reading the file.")

    except OSError as e:
        print(f"OS error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
                            

