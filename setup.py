from setuptools import setup, find_packages
import os

version = '1.0b1'

setup(name='lt.django.company',
      version=version,
      description="A Django CMS model for managing company/contact lists",
      long_description=open(os.path.join("docs", "README")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY")).read() + "\n\n" +
                       open(os.path.join("docs", "LICENSE")).read(),
      classifiers=[
        "Framework :: Django",
        "Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='django cms plugin links company contacts',
      author='LT Web Development, LLC',
      author_email='root@ltwebdev.com',
      maintainer='Benjamin Liles',
      maintainer_email='ben@ltwebdev.com',
      url='http://ltwebdev.com',
      license='MIT',
      packages=find_packages(),
      namespace_packages=['lt', 'lt.django'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'django>=1.1.1',
          'django-cms>=2.0,<3',
          'sorl-thumbnail>=3,<4',
          ],
      )
