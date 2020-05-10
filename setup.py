from pathlib import Path
import setuptools

project_dir = Path(__file__).parent

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='measure_me_bot',
    version='0.1.0',
    description='Measure Me Telegram bot',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['bot', 'telegram', 'python', 'self-help'],
    author='Sujith Sudarshan',
    url='https://github.com/sh1457/measure-me-bot.git',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=(project_dir / 'requirements.txt').read_text().split('\n'),
    zip_safe=False,
    license='MIT',
    license_files=['LICENSE.txt'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
