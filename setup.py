from setuptools import setup


setup(
    name="pydexarm",
    package_dir={"": "pydexarm"},
    py_modules=["pydexarm"],
    install_requires=["pyserial"]
)
