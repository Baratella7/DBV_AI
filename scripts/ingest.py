
from app.ingestion.pdf_loader import ler_pdf


def main():
    caminho_pdf = "data/raw/manual.pdf"

    print("Iniciando leitura do Manual Administrativo...")

    ler_pdf(caminho_pdf)

    print("\nLeitura finalizada!")


if __name__ == "__main__":
    main()
