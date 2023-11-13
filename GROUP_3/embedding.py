import random

input_code = """
def main():
    print("Done by madhu jatin venkat sahith on watermarking.")
"""

watermark = "Watermark"
keywords = ["madhu", "venkat", "jatin","sahith"]

def preprocess_code(code):
    return code.lower()

def count_characters(code):
    char_counts = [0] * 26
    for char in code:
        if char.isalpha():
            char_counts[ord(char) - ord('a')] += 1
    return char_counts

def count_keywords(code, keywords):
    keyword_counts = [0] * len(keywords)
    code = code.lower()
    for i, keyword in enumerate(keywords):
        keyword_counts[i] = code.count(keyword)
    return keyword_counts

def partition_code(code, keywords):
    partitions = code.split(watermark)
    return partitions

def embed_watermark(input_code, watermark, keywords):

    preprocessed_code = preprocess_code(input_code)

    char_counts = count_characters(preprocessed_code)

    keyword_counts = count_keywords(preprocessed_code, keywords)

    partitions = partition_code(preprocessed_code, keywords)

    key = []
    for char in watermark:
        if char in partitions:
            key.append('0')
        else:
            k = random.randint(0, 25)  
            key.append(str(k))

    OK = watermark + ''.join(key)

    return OK

output_watermark = embed_watermark(input_code, watermark, keywords)
print("Embedded Watermark (OK):", output_watermark)

#C:/Users\madhu\OneDrive\Desktop\GROUP_3\embedding.py
# Embedded Watermark (OK): Watermark90201521222822