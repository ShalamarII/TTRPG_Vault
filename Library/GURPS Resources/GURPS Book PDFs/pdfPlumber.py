import pdfplumber
import re
import json

pdf_path = r"e:\Rico Stuff\DM Folder\TTRPG Systems\GURPS\GURPS Resources\GURPS Book PDFs\GURPS - Codex Arcanum.pdf"

section_start = "Decapitation"
section_end = "Communication and Empathy Spells"  # Leave blank to go to end

# Step 1: Extract all text with page numbers
pages = []
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            pages.append({"page": i+1, "text": text})

# Step 2: Find section start and end
section_text = ""
section_start_found = False
start_page = None
for p in pages:
    if not section_start_found:
        if section_start in p["text"]:
            section_start_found = True
            start_idx = p["text"].index(section_start)
            section_text += p["text"][start_idx:]
            start_page = p["page"]
        continue
    else:
        if section_end and section_end in p["text"]:
            end_idx = p["text"].index(section_end)
            section_text += "\n" + p["text"][:end_idx]
            break
        else:
            section_text += "\n" + p["text"]

# Step 3: Split into spells
spell_start_re = re.compile(
    r"(?=^[A-Za-z' \-\\\/\(\)]+(?:\s+\w+)?\s+(Regular|Special|Missile|Blocking|Enchantment|VH|Area|Information|Resisted by [A-Za-z]+)\s*$)",
    re.MULTILINE
)
spell_chunks = spell_start_re.split(section_text)
spells_raw = []
i = 0
while i < len(spell_chunks) - 1:
    spell = spell_chunks[i] + spell_chunks[i+1]
    if i+2 < len(spell_chunks):
        body = spell_chunks[i+2]
    else:
        body = ""
    spells_raw.append((spell + "\n" + body).strip())
    i += 2

# Step 4: Parse each spell block for fields
def extract_field(pattern, text):
    match = re.search(pattern, text, re.IGNORECASE)
    return match.group(1).strip() if match else ""

def parse_spell_block(block, lines, line_to_page, start_page):
    # For page number estimation
    first_line = block.splitlines()[0].strip()
    for idx, line in enumerate(lines):
        if line.strip() == first_line:
            page_num = line_to_page[idx] if idx < len(line_to_page) else start_page
            break
    else:
        page_num = start_page

    # Define valid difficulties and spell classes
    difficulties = {"VH", "H", "A", "E", "VE"}
    spell_classes = {"Regular", "Enchantment", "Missile", "Information", "Area", "Melee", "Blocking", "Special"}

    # Parse name, difficulty, spell class
    name_line = block.splitlines()[0].strip()
    # Remove parenthetical difficulty, e.g. (VH)
    paren_diff = ""
    if "(" in name_line and ")" in name_line:
        paren_diff = name_line[name_line.find("(")+1:name_line.find(")")]
        name_line = name_line[:name_line.find("(")].strip() + name_line[name_line.find(")")+1:].strip()
    tokens = name_line.split()
    name_tokens = []
    difficulty = ""
    spell_class = ""
    for token in tokens:
        if not difficulty and (token in difficulties or token == paren_diff):
            difficulty = token
        elif not spell_class and token in spell_classes:
            spell_class = token
        else:
            name_tokens.append(token)
    name = " ".join(name_tokens).strip()

    # Extract fields flexibly
    casting_cost = extract_field(r"Base Cost:\s*([^\n,]+)", block)
    maintenance_cost = extract_field(r"Base Cost:[^\n,]+,\s*([^\n]+? to maintain)", block)
    if not maintenance_cost:
        maintenance_cost = extract_field(r"Maintenance Cost:\s*([^\n]+)", block)
    casting_time = extract_field(r"Time to Cast:\s*([^\n]+)", block)
    duration = extract_field(r"Duration:\s*([^\n]+)", block)
    prerequisites = extract_field(r"Prerequisite[s]*\s*:\s*([^\n]+)", block)

    return {
        "name": name,
        "reference": f"GOCA{page_num}",
        "difficulty": difficulty,
        "college": "Body Control",
        "power_source": "",
        "spell_class": spell_class,
        "resist": "",
        "casting_cost": casting_cost,
        "maintenance_cost": maintenance_cost,
        "casting_time": casting_time,
        "duration": duration,
        "prerequisites": prerequisites,
        "points": "1"
    }

# For page estimation
lines = section_text.splitlines()
line_to_page = []
current_page = start_page
line_count = 0
for p in pages:
    if p["page"] < start_page:
        continue
    for l in p["text"].splitlines():
        line_to_page.append(p["page"])
        line_count += 1
        if line_count >= len(lines):
            break
    if line_count >= len(lines):
        break

spells = []
for block in spells_raw:
    spells.append(parse_spell_block(block, lines, line_to_page, start_page))

# Output as JSON
with open("body_control_spells.json", "w", encoding="utf-8") as f:
    json.dump(spells, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(spells)} spells from the section '{section_start}' with page numbers and correct fields.")