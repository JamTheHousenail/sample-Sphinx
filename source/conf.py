# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GitBucket Manual'
copyright = '2024, JamTheHousenail'
author = 'JamTheHousenail'
release = '2024-03-23'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = "Sphinxでドキュメント作成"
html_theme = 'furo'
# html_theme = 'sphinx_book_theme'
html_theme_options = {
}
# html_theme_options 一覧
# https://daobook.github.io/sphinx-book-theme/customize/index.html?highlight=html_theme_options

html_static_path = ['_static']
html_css_files = ['github-markdown.css']
# html_css_files = ['custom.css']

# -- Theme ------------------------------------------------------------------

extensions = [
    'myst_parser',
    'sphinx_copybutton',
    'sphinx.ext.todo',
    'sphinx.ext.githubpages',
]

todo_include_todos = False

# pygments_style = "lightbulb"
# pygments_style = "lightbulb"

pygments_style = "xcode"
pygments_dark_style = "monokai"

# コードブロックのStyle一覧
# https://pygments.org/styles/
