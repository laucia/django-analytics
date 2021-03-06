from setuptools import setup, find_packages
 
setup(
    name='analytics',
    version='0.0.1',
    description='Basic Django Real Time analytics',
    author='Lauris Jullien',
    author_email='lauris@captain-startup.com',
    url='http://github.com/laucia/django-analytics/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)