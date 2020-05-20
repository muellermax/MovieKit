from setuptools import setup

setup(name='MovieDiary',
      version='1.1',
      description='A python class to store movies you\'ve watched',
      packages=['MovieDiary'],
      author='Maximilian Müller',
      license='MIT',
      download_url='https://github.com/muellermax/Movie-Diary/archive/1.tar.gz',
      url='https://github.com/muellermax/',
      keywords=['movie', 'diary', 'moviediary', 'statistics'],
      install_requires=['pandas', 'numpy', 'matplotlib', 'seaborn'],
      zip_safe=False)
