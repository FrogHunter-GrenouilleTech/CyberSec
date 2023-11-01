# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Cyber Security"
copyright = '2023, Poltergeist42'
author = 'Poltergeist42'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


####

extensions = [  'sphinx.ext.autodoc'
                ,'sphinx.ext.githubpages'
                ,'sphinx.ext.todo'
                ,'sphinx.ext.mathjax'
                ,"sphinx.ext.viewcode"
                ,'sphinx.ext.graphviz'
                ,'sphinxcontrib.plantuml'
                ,'sphinx_ahd_theme'
             ]

plantuml = 'java -jar /usr/share/plantuml/plantuml.jar'

plantuml_output_format = 'svg_img'
graphviz_output_format = "svg"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

## Theme : sphinx-ahd-theme
# Doc : https://sphinx.ahd-creative.agency/
# pip install sphinx-ahd-theme
# extensions = ['sphinx_ahd_theme', ...]
html_theme = 'sphinx_ahd_theme'

html_theme_options = {
    #'stickysidebar ': True, # pas supportee par nature
    'externalrefs' : 'false',
    'highlighttoc' : 'true',
    'lighter_header_decor' : 'false',
    'borderless_decor' : 'false',
    'default_layout_text_size' : '100%',
    'sidebar_master_title' : 'master title',
    'sidebar_root_title' : 'root_titer',
    'sidebar_prev_title' : 'Page précédente',
    'sidebar_next_title' : 'Page suivante',
    'max_width' : '80%'
}


# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    project_name = "Cyber Security"
    ,logo = "img/ColorLogoOpenHardware-noBackground.svg"
    ,logo_alt = "logoGrenouilleTech"
    # ,logo_height = 59
    ,logo_height = 400
    # ,logo_url = "/"
    # ,logo_width = 45
    ,logo_width = 500
)