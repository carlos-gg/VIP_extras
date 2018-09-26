"""
Convert the repo's README.md to an ipython notebook suitable for Binder.

The formatting of the README.md must be rather strict, so that this script can
recognize the paths and transform them to paths on mybinder.org

"""


import nbformat
import re


with open("../README.md") as f:
    readme = f.read()


# H1 title
readme = re.sub(r"^#\s+VIP extras",
                r"# welcome to the VIP_extra Binder!",
                readme, flags=re.MULTILINE)

# 'browse' titles
readme = re.sub(r"^##\s+\[(?P<title>.*?)\]\(./(?P<path>.*?)\)",
                r"## \g<title> [(&rarr; browse)](../../tree/\g<path>)",
                readme, flags=re.MULTILINE)

# remove binder badge
readme = re.sub(r"^\[\!\[Binder\].*",
                "",
                readme, flags=re.MULTILINE)

# tutorial sections, with GitHub link
readme = re.sub(r"^###\s+(?P<title>.*?)(?P<space>\s*\n\s*)>\s+\[GitHub\]\("
                r"./tutorials/(?P<path>.*?)\).*?$\s*$",
                r"### \g<title> [(&rarr; open)](../tutorials/\g<path>)"
                r"\g<space>",
                readme, flags=re.MULTILINE)


nb = nbformat.v4.new_notebook()
mdcell = nbformat.v4.new_markdown_cell(readme)
nb.cells.append(mdcell)

with open("../binder/welcome.ipynb", "w") as f:
    nbformat.write(nb, f)


print("successfully converted README.md to binder/welcome.ipynb.")
