# Job Recommendation System

The project aimed to build a job recommendation system using state-of-the-art NLP models and techniques. The project aimed to match resumes to job postings and identify clusters of resumes relevant to the job postings, essentially aiding in the job search process. 
* Job postings were sourced from the web using APIs, pre-processed the data using Apache Spark, and stored it in a MongoDB database. 
* Generated embeddings for all job postings using various NLP models, such as sentence transformers, and set up a parser to read resumes from PDF. 
  * NLP models considered - Word2Vec, multi-qa-mpnet-base-dot-v1 and multi-qa-MiniLM-L6-cos-v1
* Set up a framework that took a resume as input and returned all relevant job postings.
* Evaluated various NLP models and set up frameworks to assess the robustness of job matching using clustering and classification methods with SparkML.


