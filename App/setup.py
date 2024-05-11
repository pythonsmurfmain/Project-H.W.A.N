from setuptools import setup, find_packages

def load_requirements(filepath):
    with open(filepath, 'r') as f:
        requirements = f.read().splitlines()
    return requirements

setup(
    name='HWAN',
    version='1.0.0',
    author='Varil Mahere & Shashwat Singh',
    author_email='varil35414@gmail.com',
    description='Seamlessly blending the roles of a knowledgeable health navigator and an interactive Chabot , it offers unparalleled support in navigating the complexities of the healthcare landscape. This sophisticated platform provides personalized assistance, guiding users through every step of their healthcare journey.',
    url='https://github.com/pythonsmurfmain/Project-H.W.A.N.git',
    packages=find_packages(),
    install_requires=load_requirements(r'requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
