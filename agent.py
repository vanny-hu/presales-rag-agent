from utils import call_llm, chunk


def extract_info(text):

    prompt = f"""
Analizza questo testo (note o transcript).

Estrai:

- Cliente
- Contesto
- Pain points
- Needs
- Soluzioni discusse
- Vincoli

Formato chiaro e sintetico.

TESTO:
{text}
"""
    return call_llm(prompt)


def generate_presales(customer, extracted_info):

    prompt = f"""
Sei un esperto pre-sales.

Crea un documento ben strutturato e leggibile.

FORMATO OBBLIGATORIO:

==============================
PRE-SALES DOCUMENT
==============================

Cliente: {customer}

----------------------------------------
EXECUTIVE SUMMARY
----------------------------------------
...

----------------------------------------
CONTESTO CLIENTE
----------------------------------------
...

----------------------------------------
PAIN POINTS
----------------------------------------
- punto 1
- punto 2

----------------------------------------
OBIETTIVI
----------------------------------------
- ...

----------------------------------------
SOLUZIONE PROPOSTA
----------------------------------------
...

----------------------------------------
ARCHITETTURA
----------------------------------------
...

----------------------------------------
VALORE PER IL CLIENTE
----------------------------------------
- ...

----------------------------------------
RISCHI / VINCOLI
----------------------------------------
- ...

----------------------------------------
NEXT STEPS
----------------------------------------
- ...

REGOLE:
- usa bullet point
-utilizza soltanto l'ITALIANO
- linguaggio tecnico 
- non inventare informazioni, usa solo quelle estrapolate
- il presales deve essere chiaro e facile da leggere

DATI:
{extracted_info}
"""
    return call_llm(prompt)


def process_customer(customer_name, texts):

    all_chunks = []

    for t in texts:
        all_chunks.extend(chunk(t))

    extracted = [extract_info(c) for c in all_chunks]

    aggregated = "\n\n".join(extracted)

    return generate_presales(customer_name, aggregated)