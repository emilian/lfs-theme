from setuptools import setup, find_packages
import os

version = '0.8'

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()

setup(name='springshop-designs',
      version=version,
      description='Designs for SpringShop',
      long_description=README,
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Django',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
      ],
      keywords='django e-commerce online-shop',
      author='Emilian Felecan',
      author_email='emil@springmerchant.com',
      url='http://www.springshop.ro',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
      ],
      )
