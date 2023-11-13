def extraction_algorithm(Ca, KW, OK):
    Ca = Ca.lower()    

    partitions = Ca.split(KW)
    MOC_list = []
    for partition in partitions:
        counts = [0] * 26
        for char in partition:
            if char.isalpha():
                index = ord(char) - ord('a')
                counts[index] += 1
        MOC = chr(counts.index(max(counts)) + ord('a'))
        MOC_list.append(MOC)

    L1 = len(KW)
    keyindex = L1 + 1
    L2 = len(OK)
    We = []
    I = 0

    while keyindex < L2:
        if OK[keyindex] == '0':
            We.append(MOC_list[I % len(MOC_list)])
        else:
            We.append(reverse_sc(OK[keyindex]))
        keyindex += 1
        I += 1

    return ''.join(We)

def reverse_sc(char):
    k = 1 
    reversed_char = chr((ord(char) - ord('a') - k) % 26 + ord('a'))
    return reversed_char

Ca = input("Enter input Ca: ")
KW = input("Enter the keyword KW (from OK): ")
OK = input("Enter the OK: ")

output_We = extraction_algorithm(Ca, KW, OK)
print("We (Extracted Text):", output_We)

#C:\Users\madhu\OneDrive\Desktop\GROUP_3\EXTRACTION_ALGORITHM.py

# Enter input Ca: madhu jatin venkat sahith 1234
# Enter the keyword KW (from OK): keyword
# Enter the OK: keyword1357002468
# We (Extracted Text): fhjaaegik


