import re
from tqdm import tqdm
from typing import List
from dataclasses import dataclass

HTML_TO_CHAR = {
    "&amp;": "&",
    "&gt;": ">"
}


def replace_html_char(html: str):
    for html_char in HTML_TO_CHAR.keys():
        html = html.replace(html_char, HTML_TO_CHAR[html_char])
        
    return html


@dataclass
class Section:
    subject: str
    class_code: int
    name: str
    section_code: str
    crn: int
    description: str
    levels: list
    grade_basis: list
    attributes: str
    campus: str
    credits: float
    section_type: str
    time: str
    days: List[str]
    location: str
    data_range: str
    schedule_type: str
    instructors: str
    
    
def get_subject(html_block: str):
    regex = r'<a href=".+">[\s\S]+ - [0-9]{5} - ([A-Z]+) [0-9]{4}[A-Z]? - [A-Z0-9]+</a></th>'   
    match = re.search(regex, html_block)
    if match:
        return match.group(1)
    
def get_class_code(html_block: str):
    regex = r'<a href=".+">[\s\S]+ - [0-9]{5} - [A-Z]+ ([0-9]{4}[A-Z]?) - [A-Z0-9]+</a></th>'   
    match = re.search(regex, html_block)
    if match:
        return match.group(1)

def get_name(html_block: str):
    regex = r'<a href=".+">([\s\S]+) - [0-9]{5} - [A-Z]+ [0-9]{4}[A-Z]? - [A-Z0-9]+</a></th>'   
    match = re.search(regex, html_block)
    if match:
        return match.group(1)

def get_section_code(html_block: str):
    regex = r'<a href=".+">[\s\S]+ - [0-9]{5} - [A-Z]+ [0-9]{4}[A-Z]? - ([A-Z0-9]+)</a></th>'   
    match = re.search(regex, html_block)
    if match:
        return match.group(1)

def get_crn(html_block: str):
    regex = r'<a href=".+">[\s\S]+ - ([0-9]{5}) - [A-Z]+ [0-9]{4}[A-Z]? - [A-Z0-9]+</a></th>'   
    match = re.search(regex, html_block)
    if match:
        return match.group(1)

def get_description(html_block: str):
    regex = r'<td class="dddefault">\n([\s\S]*)\n<br/>\n<span class="fieldlabeltext">Associated Term:'
    match = re.search(regex, html_block)
    if match:
        match = match.group(1)
        match = replace_html_char(match)
        return match

def get_levels(html_block: str):
    regex = r'<span class="fieldlabeltext">Levels: </span>(.*)'
    match = re.search(regex, html_block).group(1).strip()
    match = match.split(", ")
    return match

def get_grade_basis(html_block: str):
    regex = r'<span class="fieldlabeltext">Grade Basis: </span>(.*)'
    match = re.search(regex, html_block).group(1).strip()
    match = list(match)
    return match

def get_attributes(html_block: str):
    regex = r'<span class="fieldlabeltext">Attributes: </span>(.*)'
    match = re.search(regex, html_block)
    
    if not match:
        return 
    
    match = match.group(1).strip()
    match = replace_html_char(match)
    
    # Edge case: "Engr, &amp;Sciences"
    if "Engr, &Sciences" in match:
        match = match.replace("Engr, &Sciences", "Engr & Sciences")
        
    match = match.split(", ")
    
    return match

def get_campus(html_block: str):
    regex = r'<br[/]?>[\s\S]<br/>[\s\S](.*)[\s\S]<br/>'
    match = re.search(regex, html_block).group(1).strip()
    match = replace_html_char(match)
    return match

def get_credits(html_block: str):
    regex = r'<br/>[\s\S](.*) Credits[\s\S]<br/>[\s\S]'
    match = re.search(regex, html_block).group(1)
    
    # Edge case: 1.000 TO       12.000 Credits
    match = match.split(" TO ")[0]
    
    # Edge case: 0.000 OR        3.000
    match = match.split(" OR ")[0]
    
    match = float(match)
    return match

def get_section_type(html_block: str):
    regex = r'<tr>' \
        + r'[\s\S]<td class="dddefault">(.*)</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]</tr>[\s\S]</table>'
    match = re.search(regex, html_block)
    if match:
        match = match.group(1).strip()
        return match

def get_time(html_block: str):
    regex = r'<tr>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">(.*)</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]</tr>[\s\S]</table>'
    match = re.search(regex, html_block)
    if not match:
        return
    
    match = match.group(1).strip()
        
    # Edge case: <abbr title="To Be Announced">TBA</abbr>
    if "TBA" in match:
        return "TBA"
        
    return match

def get_days(html_block: str):
    regex = r'<tr>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">(.*)</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]</tr>[\s\S]</table>'
    match = re.search(regex, html_block)
    if match:
        match = match.group(1).strip()
        return list(match)

def get_location(html_block: str):
    regex = r'<tr>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">(.*)</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]</tr>[\s\S]</table>'
    match = re.search(regex, html_block)
    if not match:
        return
    match = match.group(1).strip()
    
    # Edge case: <abbr title="To Be Announced">TBA</abbr>
    if "TBA" in match:
        return "TBA"
        
    return match

def get_date_range(html_block: str):
    regex = r'<tr>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">(.*)</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]</tr>[\s\S]</table>'
    match = re.search(regex, html_block)
    if match:
        match = match.group(1).strip()
        return match

def get_schedule_type(html_block: str):
    regex = r'<tr>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">(.*)</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]</tr>[\s\S]</table>'
    match = re.search(regex, html_block)
    
    if match:
        match = match.group(1).strip()
        
        # If match ends with a *, remove it
        if match[-1] == "*":        
            match = match[:-1]
            
        return match

def get_instructors(html_block: str):
    regex = r'<tr>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">.*</td>' \
        + r'[\s\S]<td class="dddefault">(.*)</td>' \
        + r'[\s\S]</tr>[\s\S]</table>'
    match = re.search(regex, html_block)
    
    if match:
        match = match.group(1)
        
    else:
        return None
    
    regex = r'target="([^"]*)'
    match = re.findall(regex, match)
    
    return match

        
def extract_section_data(html_block: str):    
    try:
        return Section(
            subject         = get_subject(html_block),
            class_code      = get_class_code(html_block),
            name            = get_name(html_block),
            section_code    = get_section_code(html_block),
            crn             = get_crn(html_block),
            description     = get_description(html_block),
            levels          = get_levels(html_block),
            grade_basis     = get_grade_basis(html_block),
            attributes      = get_attributes(html_block),
            campus          = get_campus(html_block),
            credits         = get_credits(html_block),
            section_type    = get_section_type(html_block),
            time            = get_time(html_block),
            days            = get_days(html_block),
            location        = get_location(html_block),
            data_range      = get_date_range(html_block),
            schedule_type   = get_schedule_type(html_block),
            instructors     = get_instructors(html_block),
        )
    except Exception as e:
        print("Error in HTML block:")
        print(html_block)
        raise e


def extract_data(html: str):
    sections = []
    
    # Split the HTML file at each <th class="ddtitle"> element

    print(type(html))
    html_blocks = html.split("<th class=\"ddtitle\" scope=\"colgroup\">")
    print(len(html_blocks), "HTML blocks found.")
    
    # Remove first block
    html_blocks = html_blocks[1:]
    
    print("Extracting data from HTML section blocks...")
    for html_block in tqdm(html_blocks):
        section = extract_section_data(html_block)
        sections.append(section)

    return sections
