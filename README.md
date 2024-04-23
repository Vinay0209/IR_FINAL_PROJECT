# INFORMATION RETRIEVAL PROJECT REPORT

## NAME: YERRAM VINAY
## HAWK ID: A20554778

# Abstract:
This project presents a web document crawler and search engine built using Python libraries (Scrapy, Scikit-learn, Flask). The crawler fetches web documents based on a seed URL, maximum pages, and depth. The downloaded HTML content is indexed using an inverted index with TF-IDF weighting for terms and cosine similarity for retrieval. A Flask-based processor handles user queries in JSON format, validates them, and returns top-K ranked documents based on relevance. Additionally, the report explores optional functionalities like concurrent scraping with AutoThrottle, distributed crawling with Scrapyd, word2vec embedding representation, and kNN similarity with FAISS for advanced search.

## Overview

This search engine leverages a three-tier architecture:

1. **Scrapy Crawler**: Scrapy efficiently navigates websites, downloads HTML documents based on user-defined parameters, and respects robots.txt limitations. *(Optional: Concurrent crawling with AutoThrottle or distributed crawling with Scrapyd can be implemented for larger crawls.)*

2. **Scikit-learn Indexer**: Scikit-learn constructs an inverted index from the downloaded documents. Each term in the index maps to a list of documents where it appears, along with its TF-IDF score representing its importance within each document.

3. **Flask Processor**: Flask facilitates communication with the user. It accepts free-text queries in JSON format, validates them for errors, interacts with the inverted index for retrieval, and returns the top-K most relevant documents based on cosine similarity. *(Optional: Query spelling correction with NLTK or query expansion with WordNet can be implemented for enhanced user experience.)*

## Design

### Scrapy Crawler:
The crawler utilizes Scrapy's functionalities to follow website links, extract HTML content, and handle page limitations. It respects robots.txt guidelines to avoid excessive website requests.

### Scikit-learn Indexer:
Scikit-learn's text processing tools are used to build the inverted index. Terms are extracted from documents, tokenized (broken down into meaningful units), and weighted using TF-IDF (Term Frequency-Inverse Document Frequency) to represent their importance. During retrieval, cosine similarity between the query and documents is calculated to rank their relevance.

### Flask Processor:
Flask serves as the user interface, accepting search queries in JSON format. It validates queries for potential errors (e.g., empty query) and interacts with the inverted index to retrieve documents. Cosine similarity scores between the query and documents are calculated, and the top-K most relevant documents are returned in the response.

## Architecture

The system comprises three main components:

1. **Scrapy Crawler**: A standalone application responsible for downloading web documents.

2. **Scikit-learn Indexer**: A Python script that processes downloaded documents and builds the inverted index.

3. **Flask Processor**: A web application that accepts user queries and interacts with the inverted index for retrieval.

These components interact through well-defined interfaces. The crawler stores downloaded documents, which are then processed by the indexer to build the inverted index. The Flask processor interacts with the index to retrieve documents based on user queries.



## System Capabilities

The system can:
- Initialize a web crawl with specified seed URLs
- Extract relevant content from web documents
- Limit the number of pages to crawl while controlling crawling depth
- Construct an inverted index using TF-IDF scoring mechanism to represent documents and calculate their relevance for efficient retrieval
- Process user queries to return top-K ranked results based on relevance scores computed by the indexer

## Interactions Between Components

The web crawler interacts with the indexer by passing crawled web documents for indexing. The indexer interacts with the query processor by providing indexed documents and their relevance scores for query processing. The query processor interacts with the indexer to retrieve relevant documents based on user queries.

## Integration

Components are integrated through standardized input/output formats, ensuring seamless data exchange. The web crawler, indexer, and query processor are interconnected to enable the flow of data between them, facilitating the entire search process. Integration protocols are established to ensure smooth communication and coordination among the components during the execution of tasks.

## Software Components

Powered by Flask, the processor component manages user queries and delivers pertinent documents. It verifies the validity of queries, conducts spell checking utilizing NLTK, and offers query expansion capabilities using WordNet. Using Scikit-Learn, the indexer component builds an inverted index from the documents fetched by the crawler. It employs TF-IDF scores to signify the significance of words within documents, thereby enabling effective retrieval during searches. Making use of Scrapy, the crawler component is tasked with navigating the web, fetching web documents, and formatting them for indexing purposes. Configurable parameters include seed URLs, maximum pages, and crawling depth.

## Interfaces

### Web Crawler Interface
- Parameters: Seed URLs, maximum pages, crawling depth
- Output: Retrieved web documents

### Indexer Interface
- Input: Web documents obtained by the crawler
- Output: Inverted index with TF-IDF scores

### Processor Interface
- Input: User queries
- Output: Relevant documents
- Additional Features: Spell checking, query expansion


## Operation

### Pull code:

1. open vs code and pull the repository from github


## Run the main file


1. Execute the main.py file.


## Check Crawling Progress

Monitor the terminal to ensure all webpages are crawled until the max_pages limit (e.g., 200).

<img width="215" alt="Screenshot 2024-04-22 at 8 44 45 PM" src="https://github.com/Vinay0209/IR-final-project/assets/73889115/8ed0fd04-3e77-4c79-8a6d-85b128ea8a6e">


## Initiate Processing of Web Pages

Once processing is complete, a pickle file named `processed_data.pkl` is created to store the processed pages.
<img width="215" alt="Screenshot 2024-04-22 at 8 45 36 PM" src="https://github.com/Vinay0209/IR-final-project/assets/73889115/1cd5bfd9-56d1-4786-a4f2-f920c05ca5df">


## Submit Queries

Use the search bar to submit queries.

The system retrieves top-ranked results based on relevance scores.

<img width="964" alt="Screenshot 2024-04-22 at 8 47 21 PM" src="https://github.com/Vinay0209/IR-final-project/assets/73889115/a1d9ccd9-953f-45f7-bb3f-9bc3c339ef2b">


# Conclusion

In summary, we've successfully developed a web document retrieval system leveraging Python, Scikit-Learn, Scrapy, Flask, and NiceGUI. Our accomplishments include:

- **Efficient Web Crawling:** The system adeptly navigates web pages, capturing pertinent content within predefined constraints.

- **Accurate Indexing:** Utilizing TF-IDF scoring, we've established an inverted index that precisely reflects the significance of words in documents.

- **User-Friendly Query Processing:** The processor efficiently manages user queries, furnishing top-ranked results based on relevance scores. Integration with NiceGUI provides an aesthetically pleasing interface for monitoring web documents during crawling.

- **Storage Optimization:** By storing processed pages in a pickle file named `processed_data.pkl`, we streamline resource utilization and minimize the necessity for page reloading.

# Data Sources

- [https://www.wikihow.com/Main-Page](https://www.wikihow.com/Main-Page)

# Source Code
## Main.py
<img width="651" alt="Screenshot 2024-04-22 at 9 01 52 PM" src="https://github.com/Vinay0209/IR-final-project/assets/73889115/c4d25cfd-50d3-4b3e-acbc-51393627c8f0">

## Indexer.py
<img width="704" alt="Screenshot 2024-04-22 at 9 02 55 PM" src="https://github.com/Vinay0209/IR-final-project/assets/73889115/eabcbaf6-f208-4ca4-8ea7-90cb317729ec">

## Processor.py
<img width="624" alt="Screenshot 2024-04-22 at 9 04 26 PM" src="https://github.com/Vinay0209/IR-final-project/assets/73889115/fa672699-d231-4103-a5bf-f278298be082">

## Indexer2.py
<img width="711" alt="Screenshot 2024-04-22 at 9 11 23 PM" src="https://github.com/Vinay0209/IR-final-project/assets/73889115/b9a67704-360e-4da6-8d9a-7a022d34f434">

# Reference


1. [https://www.wikihow.com/Main-Page](https://www.wikihow.com/Main-Page)

2. Baier, H., & Zeller, A. (2019). Distributed Crawling with Scrapy. In *Proceedings of the 14th International Conference on Mining Software Repositories (MSR '17)* (pp. 89-92). DOI: [10.1109/MSR.2017.55](https://doi.org/10.1109/MSR.2017.55)

3. Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (2nd ed.). O'Reilly Media.

4. Grinberg, M. (2018). *Flask Web Development: Developing Web Applications with Python* (2nd ed.). O'Reilly Media.
   
5. Scrapy. (n.d.). In Scrapy Documentation. Retrieved from [https://docs.scrapy.org/en/latest/](https://docs.scrapy.org/en/latest/)
     
6. Scrapy GitHub Repository. (n.d.). Retrieved from [https://github.com/scrapy/scrapy](https://github.com/scrapy/scrapy)
   
7. scikit-learn. (n.d.). In Scikit-learn Documentation. Retrieved from [https://scikit-learn.org/stable/index.html](https://scikit-learn.org/stable/index.html)
    
8. Flask. (n.d.). In Flask Documentation. Retrieved from [https://flask.palletsprojects.com/en/2.0.x/](https://flask.palletsprojects.com/en/2.0.x/)
  
9. Ronacher, A. (2010). Werkzeug: The Python WSGI Utility Library. Retrieved from [https://palletsprojects.com/p/werkzeug/](https://palletsprojects.com/p/werkzeug/)







  


