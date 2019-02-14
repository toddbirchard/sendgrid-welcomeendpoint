from setuptools import setup, find_packages, tests_require, packages, name

with open("README", 'r') as f:
    long_description = f.read()

setup = (
    name='Sendgrid Welcome Email Endpoint.',
    version='1.0',
    description='Endpoint which triggers a welcome email to a newly acquired user.',
    long_description=long_description,
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    url="https://github.com/toddbirchard/sendgrid-welcomeendpoint",
    packages=['/', 'tests'],
    tests_require=["pytest"],
    cmdclass={"pytest": PyTest},
    install_requires=[
        "flask",
        "sendgrid"
    ]
)
