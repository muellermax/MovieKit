from setuptools import setup

setup(name='MovieDiary',
      version='1.0',
      description='A python class to store movies you\'ve watched',
      packages=['MovieDiary'],
      author='Maximilian Müller',
      license='MIT',
      download_url='https://github.com/muellermax/mmuda_distributions/archive/1.1.tar.gz',
      url='https://github.com/muellermax/',
      keywords=['movie', 'diary', 'moviediary', 'statistics'],
      install_requires=['pandas', 'numpy', 'matplotlib', 'seaborn', 'datetime', 'os'],
      zip_safe=False)
