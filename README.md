# Tool for Querying Database Using a Universal Natural Language Interface
Natural Language Processing can bring powerful enhancement to virtually any computer program interface. This project has been developed to generate accurate and valid SQL queries after parsing natural language using open source tools and libraries. It aims at understanding any natural language input statement and convert it to query. It involves understanding all natural languages that can be inputted by the user and finding and solving complex relationships between words and inputs given in the statement.

The NLP tools used:

SpaCy: 

spaCy is an open-source software library for advanced natural language processing, written in the programming languages Python and Cython.The library is published under the MIT license and its main developers are Matthew Honnibal and Ines Montani, the founders of the software company Explosion.
Unlike NLTK, which is widely used for teaching and research, spaCy focuses on providing software for production usage. As of version 1.0, spaCy also supports deep learning workflows[7] that allow connecting statistical models trained by popular machine learning libraries like TensorFlow, PyTorch or MXNet through its own machine learning library Thinc. Using Thinc as its backend, spaCy features convolutional neural network models for part-of-speech tagging, dependency parsing, text categorization and named entity recognition (NER). Prebuilt statistical neural network models to perform these task are available for English, German, Greek, Spanish, Portuguese, French, Italian, Dutch, Lithuanian and Norwegian, and there is also a multi-language NER model. Additional support for tokenization for more than 50 languages allows users to train custom models on their own datasets as well.

TextBlob: 

TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis, classification, translation, and more. it is a library based on NLTK and a pattern.
 NLTK3 library
 
  NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.
Thanks to a hands-on guide introducing programming fundamentals alongside topics in computational linguistics, plus comprehensive API documentation, NLTK is suitable for linguists, engineers, students, educators, researchers, and industry users alike. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source, community-driven project.

PyMysql:

To connect to the mysql database, we used PyMysql (pymysql). While it is not optimized out of the box, it can be optimized with additional tools. We chose it because it is written in python and supports python 3.6. Being written in python, it can be installed with python’s pip packaging system. We use MySql for this project for its ease of use, expressive querying language, open sourceness, and many python packages to work with it. 

