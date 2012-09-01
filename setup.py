from setuptools import find_packages
from setuptools import setup
import os


long_description = (
    open(os.path.join("collective", "cart", "stock", "docs", "README.rst")).read() + "\n" +
    open(os.path.join("collective", "cart", "stock", "docs", "HISTORY.rst")).read() + "\n" +
    open(os.path.join("collective", "cart", "stock", "docs", "CONTRIBUTORS.rst")).read())


setup(
    name='collective.cart.stock',
    version='0.1',
    description="Adds stock content type.",
    long_description=long_description,
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@gmail.com',
    url='https://github.com/collective/collective.cart.stock/',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective', 'collective.cart'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'five.grok',
        'hexagonit.testing',
        'plone.app.dexterity',
        'plone.browserlayer',
        'plone.directives.form',
        'setuptools',
        'zope.i18nmessageid'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """,)
