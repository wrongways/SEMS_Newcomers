GLOSSARY = "glossary.adoc"

glossary = {}
with open(GLOSSARY) as g:
    for line in g.readlines():
        line = line.strip()
        if "::" in line:
            print(line)
            term, defn = line.split("::")
            glossary[term] = defn


print(glossary)
with open(GLOSSARY, "w", encoding="UTF8") as g:
    g.write("[horizontal]\n")
    for k in sorted(glossary.keys()):
        g.write(f"{k.strip()}:: {glossary[k].strip()}\n")
