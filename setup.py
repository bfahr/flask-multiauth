import os
from setuptools import setup, find_packages

__here__ = os.path.dirname(os.path.abspath(__file__))

runtime = {
    'pyyaml',
    'requests',
    'requests_kerberos',
    'flask',
    'Jinja2',
    'Flask-RESTful',
    'Flask-SQLAlchemy',
    'MySQL-python',
    'SQLAlchemy',
    'gunicorn',
    'flask-ldap',
    'flask-session',
    'kerberos',
    'pycrypto',
}

develop = {
    'flake8',
    'coverage',
    'pytest',
    'pytest-cov',
    'Sphinx',
    'sphinx_rtd_theme',
}

if __name__ == "__main__":
    # allows for runtime modification of rpm name
    name = "test"

    try:
        setup(
            name=name,
            version="0.0.1",
            description="Insights RuleAnalysis Services",
            packages=find_packages(),
            include_package_data=True,
            install_requires=list(runtime),
            extras_require={
                'develop': list(runtime | develop),
                'optional': ['python-cjson', 'python-logstash', 'python-statsd', 'watchdog'],
            },
        )
    finally:
        pass