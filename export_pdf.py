from fpdf import FPDF

def export_pdf(results, filename='scan_report.pdf'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Web Pentest Framework Scan Report", ln=True, align='C')
    pdf.ln(10)
    for item in results:
        pdf.multi_cell(0, 10, txt=f"{item['type']}: {item['details']}")
    pdf.output(filename)