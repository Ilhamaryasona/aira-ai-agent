from langchain.agents import Tool
from citation import apa_citation, harvard_citation

def academic_writer(text):
    return f"Teks akademik terstruktur:\n{text}"

def generate_citation(style, author, year, title, journal, volume=None, issue=None, pages=None):
    if style.lower() == "apa":
        return apa_citation(author, year, title, journal, volume, issue, pages)
    elif style.lower() == "harvard":
        return harvard_citation(author, year, title, journal, volume, issue, pages)
    else:
        return "Gunakan gaya APA atau Harvard."

tools = [
    Tool(
        name="AcademicWriter",
        func=academic_writer,
        description="Menyusun tulisan ilmiah"
    ),
    Tool(
        name="CitationGenerator",
        func=generate_citation,
        description="Membuat sitasi APA atau Harvard"
    )
]
