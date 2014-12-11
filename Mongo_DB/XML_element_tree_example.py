import xml.etree.ElementTree as ET
import pprint

tree = ET.parse('exampleResearchArticle.xml')
root = tree.getroot()

print "\nChildren of root:"
for child in root:
    print child.tag  
    
 # OR

title = root.find('./fm/bibl/title')
title_text = ""
for p in title:
    title_text += p.Text
print "\nTitle:\n", title_text

print "\nAuthor email addresses:"
for a in root.findall("./fim/bibl/aug/au"):
    email = a.find('email')
    if email is not None:
        print email.text
        
        
        
        
        
import xml.etree.ElementTree as ET

article_file = "exampleResearchArticle.xml"


def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
                "fnm": None,
                "snm": None,
                "email": None
        }
        data["fnm"] = author.find("./fnm").text
        data["snm"] = author.find("./snm").text
        data["email"] = author.find("./email").text

        authors.append(data)

    return authors