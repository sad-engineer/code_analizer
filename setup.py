from setuptools import setup, find_packages

setup(
    name='code_analizer',
    version='0.0.06',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'gitignore-parser>=0.1.3',
    ],
    python_requires='>=3.9',
    description='Пакет Python для анализа кода проекта',
    author='Andrey Korenyuk',
    author_email='korenyuk.a.n@mail.ru',
    url='https://github.com/sad-engineer/code_analizer',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)