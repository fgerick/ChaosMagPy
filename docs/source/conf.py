# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, root)
autodoc_mock_imports = ['_tkinter']

import matplotlib  # import so that 'agg' can be given, as readthedocs fails
import matplotlib.pyplot as plt
matplotlib.use('agg')
plt.ioff()

import datetime
import chaosmagpy

# -- Project information -----------------------------------------------------

project = 'ChaosMagPy'
copyright = str(datetime.date.today().year) + ', Clemens Kloss'
author = 'Clemens Kloss'

# The short X.Y version
version = chaosmagpy.__version__
# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'numpydoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx_gallery.gen_gallery',
    'matplotlib.sphinxext.plot_directive',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'nature'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['.static']

# add button to hide prompts and outputs in code examples
# also required "copybutton.js" and "jquery.js" in .static directory
def setup(app):
    app.add_js_file('copybutton.js')

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.

html_sidebars = {'**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ChaosMagPydoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'chaosmagpy.tex', 'ChaosMagPy Documentation',
     'Clemens Kloss', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'chaosmagpy', 'ChaosMagPy Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'chaosmagpy', 'ChaosMagPy Documentation',
     author, 'ChaosMagPy', 'Package to read the CHAOS model and '
     'compute the geomagnetic field.',
     'Miscellaneous'),
]


# -- Extension configuration -------------------------------------------------

# -- Options for autodoc extension ---------------------------------------

# generate rst of member functions on the fly
autosummary_generate = True
autodata_content = 'both'

# -- Options for numpydoc extension ---------------------------------------

# Remove class members to suppress error message when compiling
# (removes module list)
numpydoc_show_class_members = True
numpydoc_show_inherited_class_members = False
numpydoc_class_members_toctree = False

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Options for sphinx gallery ----------------------------------------------

sphinx_gallery_conf = {
     'examples_dirs': '.static/examples',   # path to your example scripts
     'gallery_dirs': 'gallery',  # path to gallery generated output

     'download_all_examples': False,
}

# -- Matplotlib plot_directive options ---------------------------------------

plot_pre_code = ''
plot_include_source = True
plot_formats = [('png', 96)]
plot_html_show_formats = False
plot_html_show_source_link = False

fontsize = 13*72/96.0  # 13 px

plot_rcparams = {
    'font.size': fontsize,
    'axes.titlesize': fontsize,
    'axes.labelsize': fontsize,
    'xtick.labelsize': fontsize,
    'ytick.labelsize': fontsize,
    'legend.fontsize': fontsize,
    'figure.figsize': (5*1.618, 5),
    'text.usetex': False,
}
