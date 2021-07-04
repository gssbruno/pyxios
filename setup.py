import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyxios-bgss',
    version="1.0.0",
    author="Bruno Santos",
    author_email="b.g.santos@outlook.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/gssbruno/pyxios',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    python_require=">=3.6"
)
