import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # Ensure your project is importable

project = 'My Project'
author = 'Your Name'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',  # Auto-generates API documentation from docstrings
    'sphinx.ext.napoleon',  # Supports Google-style and NumPy-style docstrings
    'sphinx.ext.viewcode',  # Adds source code links
]

html_theme = 'sphinx_rtd_theme'  # Use Read the Docs theme
