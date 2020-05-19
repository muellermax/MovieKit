# Movie Diary


### About

Movie Diary is a python class to store the movies you've watched in a pandas dataframe and in a csv-file. Furthermore, it includes information about this movie like a personal evaluation, where you've watched it and the category (e.g. cinema, netflix, etc.). 


### Installation

The Movie Diary is not yet on Pypi yet. 


### Dependencies

Movie Diary requires the following python libraries: datetime, matplotlib, os, pandas, seaborn. 


### Methods

The class has currently the following methods: 
* `add_movie`: Add a movie to an existing dataframe and csv file and provide detail information (location, category, evaluation). If the csv does not exist yet, it creates a new one. 
* `delete_diary`: Delete the existing csv-file. Not recommended. 
* `plot_top_movies_time`: Create a Seaborn Scatterplot with the 30 most watched movies over time. The category and the evaulation are also included in the scatterplot as hue and bubble-size. 


### Author

Maximilian Müller, Business Development Manager in the Renewable Energy sector. Now diving into the field of data analysis.
GitHub: https://github.com/muellermax
LinkedIn: https://www.linkedin.com/in/maximilian-m%C3%BCller-92106067/
Kaggle: https://www.kaggle.com/muellermax


### License

Copyright 2020 Maximilian Müller

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

From opensource.org

