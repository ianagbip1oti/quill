from setuptools import setup

setup(name="quill",
      version="1.9.0",
      description="A Python library used to create text-based games with TkInter.",
      author="DeflatedPickle",
      author_email="DeflatedPickle@gmail.com",
      url="https://github.com/DeflatedPickle/adventure",
      license="MIT",
      setup_requires = [
          "pytest-runner==2.11.1"
      ],
      tests_require = [
          "pytest==3.0.7",
          "pytest-cov==2.4.0"
      ],
      classifiers=[
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
      ],
      keywords=["quill", "text-based", "adventure", "game", "GUI", "window"],
      packages=["quill"])
