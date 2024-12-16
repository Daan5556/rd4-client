from setuptools import setup, find_packages

setup(
    name='rd4_client',
    version='0.1.0',  # Start with a semantic version
    description='A simple client for RD4 waste calendar',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/daan5556/rd4-client',  # Replace with your repo
    author='Daan Eggen',
    author_email='egdaan@gmail.com',
    license='MIT',  # Replace if using another license
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'certifi==2024.12.14',
        'charset-normalizer==3.4.0',
        'idna==3.10',
        'requests==2.32.3',
        'setuptools==75.6.0',
        'urllib3==2.2.3',
    ],
)
