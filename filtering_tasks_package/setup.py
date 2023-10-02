from setuptools import setup, find_packages

setup(
    name="Filtering_Task_package",
    version="0.1",
    packages=find_packages(),
    install_requires=["numpy", "pytest"],  # Add any dependencies here
    author="Onyero Walter Ofuzim",
    description="Package for filtering SLA data for the weekly SLA utilization report",
)
