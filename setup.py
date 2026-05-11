"""
Setup configuration for packaging and distributing the Fantasy Cricket Game.
"""

from setuptools import setup

setup(
    name="FantasyCricketGame",
    version="1.0",
    description="Fantasy Cricket desktop application built using Python, PyQt5, and SQLite",
    author="Artham Siri",
    py_modules=["Main", "EvaluateTeam"],
    install_requires=[
        "PyQt5==5.15.9"
    ],
)
