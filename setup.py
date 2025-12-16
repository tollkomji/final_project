from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='1.0.0',
    author='Your Name',
    description='A package for emotion detection in text using Watson NLP',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
    ],
    python_requires='>=3.6',
)