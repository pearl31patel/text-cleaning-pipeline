import re

stopwords = {"is", "am", "are", "the", "and", "to", "of", "in", "for", "on", "at"}

def text_cleaning_pipeline(text):
    text = text.lower()
    text = re.sub(r"https?://\S+|www\.\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"\S+@\S+", "", text)
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    
    words = text.split()
    words = [w for w in words if w not in stopwords]
    
    return " ".join(words)

def process_data(data):
    return [text_cleaning_pipeline(text) for text in data]

n = int(input("Enter number of sentences: "))

data = []
for i in range(n):
    text = input(f"Enter sentence {i+1}: ")
    data.append(text)

clean_data = process_data(data)

print("\n Output after cleaning the original text :")
for t in clean_data:
    print(t)
