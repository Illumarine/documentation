import markdown2
from pdfitdown.pdfconversion import Converter
import tomllib
import os

data = 0
with open("./docs/_index.toml", "rb") as inp:
  data = tomllib.load(inp)

file_list = data["files"]

# build HTML
for file_name in file_list:
  export_as = file_name.replace(".md", ".html")
  export_content = ""
  with open(f"./docs/{file_name}", "r") as mdinp:
    export_content = markdown2.markdown(mdinp.read())
  try:
    os.mkdir("html")
  except: 
    pass
  with open(f"./html/{export_as}", "w") as htmlout:
    htmlout.write(export_content)

# build PDF
omni_md = ""
for file_name in file_list:
  export_content = ""
  with open(f"./docs/{file_name}", "r") as mdinp:
    export_content = mdinp.read()
  omni_md += export_content + "\n\n"
  
with open("omni.md", "w") as omni:
  omni.write(omni_md)

convert = Converter()
try:
  os.mkdir("pdf")
except: 
  pass
convert.convert(file_path="omni.md", output_path="pdf/docs.pdf")