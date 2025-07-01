from fpdf import FPDF

# Create a new PDF document using FPDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, 'AKASH NITIN GADHAVE', ln=True, align='C')
        self.set_font('Arial', '', 11)
        self.set_text_color(0, 0, 0)
        self.cell(0, 7, 'Python Developer', ln=True, align='C')
        self.cell(0, 7, '📞 9834740096 | 📧 akashgadhave8624@gmail.com | 📍 Hadapsar, Pune', ln=True, align='C')
        self.cell(0, 7, 'GitHub: your_github_link', ln=True, align='C')
        self.ln(5)

    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(0, 51, 102)
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)

    def section_body(self, text):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 7, text)
        self.ln(1)

# Create PDF instance and add content
pdf = PDF()
pdf.add_page()

# Professional Summary
pdf.section_title("PROFESSIONAL SUMMARY")
pdf.section_body(
    "Results-driven and detail-oriented Python Developer with a strong academic foundation and hands-on experience in backend development, "
    "data analysis, and full-stack applications. Proficient in leveraging Python and data visualization tools to deliver actionable business insights. "
    "Skilled in Django, SQL, and modern data libraries such as Pandas and Seaborn. Demonstrated success in analyzing complex datasets, building "
    "analytical pipelines, and delivering clean, visual reports that support decision-making across business and healthcare domains. "
    "Committed to continuous learning, clean code, and scalable software solutions."
)

# Technical Skills
pdf.section_title("TECHNICAL SKILLS")
pdf.section_body(
    "- Languages & Tools: Python, SQL, HTML, CSS, JavaScript\n"
    "- Frameworks/Libraries: Django, Pandas, NumPy, Matplotlib, Seaborn\n"
    "- Visualization Tools: Power BI, Excel\n"
    "- Databases: MySQL, SQLite\n"
    "- Version Control: Git, GitHub"
)

# Projects
pdf.section_title("PROJECTS")
pdf.section_body(
    "Regional Sales Data Analysis (Acme Co.)\n"
    "Tools: Python, Pandas, NumPy, Seaborn, Power BI\n"
    "- Performed EDA on five years of sales data to uncover regional performance, product profitability, and seasonal trends.\n"
    "- Merged and transformed datasets related to sales, customers, products, and budgets.\n"
    "- Built visualizations and provided insights that informed Power BI dashboard development.\n\n"

    "Patient Encounter & Flow Analysis\n"
    "Tools: Python, Pandas, Matplotlib, Seaborn\n"
    "- Developed a data pipeline to analyze patient visit data across healthcare organizations.\n"
    "- Merged multiple datasets (encounters, procedures, payers, patients) and created features like encounter duration and payer coverage.\n"
    "- Uncovered trends and anomalies to assist with operational decisions and cost analysis.\n\n"

    "Diwali Sales Analysis\n"
    "Tools: Python, Pandas, Matplotlib\n"
    "- Analyzed customer purchase patterns and product performance during Diwali season.\n"
    "- Provided insights for marketing and inventory strategies based on customer segmentation and sales peaks.\n\n"

    "Omni Food Delivery App\n"
    "Tools: HTML, CSS, JavaScript\n"
    "- Created a responsive food delivery web app with order tracking and menu browsing functionality.\n"
    "- Focused on UX/UI and usability for a seamless customer experience."
)

# Education
pdf.section_title("EDUCATION")
pdf.section_body("Bachelor of Computer Applications\nTerna Mahavidyalaya, BAMU University\n\nDiploma | SSC")

# Languages
pdf.section_title("LANGUAGES")
pdf.section_body("English (Fluent), Hindi, Marathi")

# Save the PDF
output_path = "/mnt/data/Akash_Gadhave_ATS_Resume.pdf"
pdf.output(output_path)
output_path
