import pdfplumber
import csv
import sys
def extract_professores (pdf_path):
    matriculas = set()
    with pdfplumber.open(pdf_path)as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                
                lines = text.split("\n")
                for line in lines:
                    if line.isdigit():
                        matriculas.add(line)
        return matriculas 
    def save_csv (matriculas):

        with open("professores.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(["matricula"])

            for m in matriculas:
                writer.writerow([m])
    if __name__ == "__main__":

        pdf_file = sys.argv[1]

        matriculas = extract_professores(pdf_file)

        save_csv(matriculas)

        print("Extração concluída")

        
