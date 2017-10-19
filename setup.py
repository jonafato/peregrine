from setuptools import setup, find_packages
setup(
    name='peregrine',
    version="0.1dev",
    description='Peregrine is an opinioned blog system for the Wagtail content management system on the Django Web Framework.',
    author='Tim Allen',
    author_email='tallen@wharton.upenn.edu',
    url='https://github.com/FlipperPA/peregrine',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'wagtail>=1.8',
        'wagtailcontentstream',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)