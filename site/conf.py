# copyright = u'2022, Amazon Web Services'
# author = u'Amazon Web Services'

# -- General configuration ------------------------------------------------

extensions = ["myst_parser", "sphinx_toolbox.collapse"]

pygments_style = "default"
pygments_dark_style = "gruvbox-dark"

todo_include_todos = False
smartquotes = False
nitpicky = True

# -- Options for HTML output ----------------------------------------------

html_title = "Beginning Python"
html_theme = "furo"
language = "en"

html_static_path = ["./static"]
html_css_files = ["custom.css", "student.css"]

# Theme similar to smithy.io and gruvbox with help from https://m2.material.io/design/color/the-color-system.html#tools-for-picking-colors
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#f45429",
        "color-brand-content": "#724bff",
        "color-highlight-on-target": "#FFD9CD",
        "color-admonition-title--important": "#FF52A9",
        "color-admonition-title-background--important": "#FF52A925",
    },
    "dark_css_variables": {
        "color-brand-primary": "#ffaa22",
        "color-brand-content": "#7aadd4",
        "color-highlight-on-target": "#ffaa2233",
        "color-admonition-title--important": "#FF52A9",
        "color-admonition-title-background--important": "#FF52A925",
    },
}
