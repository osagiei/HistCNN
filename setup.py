from setuptools import setup

setup(name='histcnn',
      version='0.0',
      description='Library for running CNN on histology images.',
      url='https://github.com/javadnoorb/HistCNN',
      author='Javad Noorbakhsh',
      author_email='javad.noorbakhsh@jax.org',
      license='Apache 2.0',
      packages=['histcnn'],
      package_data={'histcnn': ['data/*', 'data/graphs/*']},
      package_dir = {'': 'src'},
      scripts=['src/histcnn/histcnn'],
      install_requires=open("REQUIREMENTS.txt").readlines(),
      zip_safe=False)
