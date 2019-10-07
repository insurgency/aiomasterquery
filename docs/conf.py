project = 'aiomasterquery'
# noinspection PyShadowingBuiltins
copyright = '2019, insurgency.gg'
author = 'insurgency.gg'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_theme = 'alabaster'
html_static_path = ['_static']
extlinks = {
    'valve-wiki': ('https://developer.valvesoftware.com/wiki/%s', 'page'),
    'steam-app': ('https://store.steampowered.com/app/%s', 'app-id'),
}
