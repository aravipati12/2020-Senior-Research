# Developing an Automated Algorithm for Transcribing and Summarizing Videos


## Overview

### Motivation

* **Issue:** billions of gigabytes of videos produced daily
* **Audience:** everyday digital citizens
* **Need:** concise, accurate summaries
* **Purpose:** quickly gauging content’s value

### Proposed Solution

We will develop an algorithm to streamline and automate the process of **transcribing** and **summarizing** speech in TED talks using Google Cloud Speech to Text API and natural language processing (NLP).

## Requirements

* Google Cloud Speech to Text API
* Pydub
* NLTK
* NumPy

## Installation Instructions

* Google Cloud Speech to Text API - Make an Account using your Google Account, Download Account Info in JSON File and Download Packages Using Homebrew
* Pydub - Install Using Homebrew
* NumPy - Install Using Homebrew

## Run Instructions

* Run google_stt.py with an audio file that is stored in an audio folder as the input in Terminal (ex. python3 google_stt.py speech.mp3)
** The audio file must have only ONE audio channel.
* Run test.py in Terminal (ex. python3 test.py)

## Sample Output

From summary.txt:

Like other predominantly black churches across the country Trinity embodies
the black community in its entirety the doctor and the welfare mom the model
student and the former gangbanger. The press has scoured every exit poll for
the latest evidence of racial polarization not just in terms of white and
black but black and brown as well. I am the son of a black man from Kenya and
a white woman from Kansas. A lack of economic opportunity among black men and
the shame and frustration that came from not being able to provide for ones
family contributed to the erosion of black families a problem that welfare
policies for many years may have worsened.

## Acknowledgments
The authors would like to acknowledge TJHSST Computer Systems Lab Director Dr. Patrick White for his guidance and support as our research mentor.

## Authors
- [@arnavbansal1](https://github.com/arnavbansal1)
- [@aravipati12](https://github.com/aravipati12)
