# Lib
from setuptools import setup, find_packages
exec(open('methylcheck/version.py').read())

# note: ANY param must fit on a single line or twine breaks.
setup(
    name='methylcheck',
    version=__version__,
    description="""Quality Control (QC), Visualization/plotting, and postprocessing software for Illumina methylation array data. See https://life-epigenetics-methylcheck.readthedocs-hosted.com/en/latest/ for full documentation and examples.""",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    project_urls = {
        "Documentation": "https://life-epigenetics-methylcheck.readthedocs-hosted.com/en/latest/",
        "Source": "https://github.com/FOXOBioScience/methylcheck/",
        "Funding": "https://FOXOBioScience.com/"
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Framework :: Jupyter',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
      ],
    keywords='methylation dna data processing epigenetics illumina',
    url='https://github.com/FOXOBioScience/methylcheck',
    license="MIT License",
    author='Life Epigenetics',
    author_email='info@FOXOBioScience.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'statsmodels',
        'matplotlib',
        'seaborn',
        'tqdm',
    ],
    extras_require={
        'dev': [
            'methylprep', # this is not REQUIRED but some functions in unit testing do require it, so in extras.
            'joblib', # used by MDS only
            'sklearn', # used by MDS only
            'pytest',
            'pytest-pep8',
            'pytest-cov',
            'flake8',
            'pytest',
            'coverage',
            'xlrd',
            'python-coveralls',
            'sphinxcontrib-apidoc',
            'm2r',
            'nbsphinx',
            'sphinx',
            'ipykernel'
        ]
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'methylcheck-cli = methylcheck.cli:cli_parser',
            ],
    }
)
