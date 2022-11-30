from setuptools import find_packages, setup

# with open("README.md", "r") as file:
#     LONG_DESCRIPTION = file.read()

# with open("requirements.txt", "r") as file:
#     DEPENDENCIES = file.readlines()

setup(
    name="mkdocs-social-buttons-plugin",
    version="0.1",
    description="Mkdocs plugin that generates inline social sharing buttons.",
    # long_description=LONG_DESCRIPTION,
    # long_description_content_type="text/markdown",
    keywords="mkdocs social plugin",
    project_urls={
        "Source": "https://github.com/richardforshaw/mkdocs-social-buttons-plugin"
    },
    author="Richard Forshaw",
    author_email="richard@forshaw.org",
    include_package_data=True,
    license="MIT",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # install_requires=DEPENDENCIES,
    # packages=find_packages(),
    entry_points={
        "mkdocs.plugins": [
            "social-buttons = mkdocs_social_buttons_plugin.plugin:SocialButtonsPlugin"
        ]
    }
)
