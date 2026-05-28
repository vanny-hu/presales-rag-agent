import subprocess
import os


def call_llm(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    return result.stdout.decode()


def load_customer_files(folder):
    texts = []

    # 🔥 legge anche sottocartelle (notes/, transcripts/, ecc.)
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(root, file)

                with open(path, encoding="utf-8") as f:
                    texts.append(f.read())

    return texts


def chunk(text, size=1000):
    return [text[i:i+size] for i in range(0, len(text), size)]


def clean_text(text):
    # ✅ rimuove caratteri invalidi
    return "".join(
        c for c in text
        if c.isprintable() or c in "\n\t"
    )


def save_txt(customer_path, content):
    

    presales_dir = os.path.join(customer_path, "presales")
    os.makedirs(presales_dir, exist_ok=True)

    # pulizia
    content = "".join(
        c for c in content
        if c.isprintable() or c in "\n\t"
    )

    
    final_content = f"""
========================================
        GENERATED PRE-SALES DOCUMENT
========================================

{content}
"""

    output_path = os.path.join(presales_dir, "presales.txt")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_content.strip())
