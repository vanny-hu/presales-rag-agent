import os
from utils import load_customer_files, save_txt
from agent import process_customer


def run():

    base_path = "Client"

    for customer in os.listdir(base_path):

        customer_path = os.path.join(base_path, customer)

        if not os.path.isdir(customer_path):
            continue

        print(f"\n🔄 Processing {customer}...")

        texts = load_customer_files(customer_path)

        if not texts:
            print("⚠️ No files found, skipping")
            continue

        try:
            presales_doc = process_customer(customer, texts)

            save_txt(customer_path, presales_doc)

            print(f"✅ Presales salvato per {customer}")

        except Exception as e:
            print(f"❌ Errore su {customer}: {e}")


if __name__ == "__main__":
    run()