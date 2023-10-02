from setuptools import setup, find_packages

setup(
    name="filtering_task_package",
    version="0.0.1",
    description="Package for filtering SLA data for the weekly SLA utilization report",
    author="Onyero Walter Ofuzim",
    author_email="onyero.ofuzim@eng.uniben.edu",
    packages=find_packages(),
    # packages=["filtering_task_package"],
    install_requires=["numpy", "pytest"]  # Add any dependencies here
)
