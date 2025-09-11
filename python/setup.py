
from setuptools import setup, find_packages

setup(
	name="latenzy",
	version="0.1.0",
	description="Python tools for latenZy analysis",
    long_description="latenzy.py\n\n"
                "Contains latenzy and latenzy2 to compute latencies for spiking responses\n"
                "See Haak et al. 2025\n\n"
                "2025, Alexander Heimel, translated from MATLAB version by Robin Haak",
	author="Herseninstituut",
	url="https://github.com/Herseninstituut/latenZy",
	packages=find_packages('.'),
    package_dir={'': '.'},
	install_requires=[],  # Add dependencies here if needed
	python_requires=">=3.7",
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
        "Intended Audience :: Science/Research", 
        "Topic :: Scientific/Engineering :: Bio-Informatics", 
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
	],
	include_package_data=True,
	zip_safe=False,
)
