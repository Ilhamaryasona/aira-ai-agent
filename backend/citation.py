def apa_citation(author, year, title, journal, volume=None, issue=None, pages=None):
    text = f"{author} ({year}). {title}. {journal}"
    if volume:
        text += f", {volume}"
    if issue:
        text += f"({issue})"
    if pages:
        text += f", {pages}"
    return text + "."

def harvard_citation(author, year, title, journal, volume=None, issue=None, pages=None):
    text = f"{author}, {year}. {title}. {journal}"
    if volume:
        text += f", {volume}"
    if issue:
        text += f"({issue})"
    if pages:
        text += f", pp. {pages}"
    return text + "."
