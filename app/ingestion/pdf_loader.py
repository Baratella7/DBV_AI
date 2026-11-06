
import fitz


def ler_pdf(caminho_pdf):
    documento = fitz.open(caminho_pdf)

    print(f"Total de páginas: {len(documento)}")

    for numero, pagina in enumerate(documento, start=1):
        texto = pagina.get_text("text")

        print(f"\n--- Página {numero} ---")
        print(texto[:300])

    documento.close()
