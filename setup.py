from setuptools import setup

setup(name='MovieKit',
      version='1.0',
      description='A python package to store movies you\'ve watched',
      packages=['MovieKit'],
      author='Maximilian Müller',
      license='MIT',
      download_url='https://github.com/muellermax/Movie-Diary/archive/1.1.tar.gz',
      url='https://github.com/muellermax/',
      keywords=['movie', 'MovieKit', 'diary', 'moviediary', 'statistics'],
      install_requires=['pandas', 'numpy', 'matplotlib', 'seaborn'],
      zip_safe=False)
