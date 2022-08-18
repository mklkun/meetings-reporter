![License MIT](https://img.shields.io/badge/License-MIT-blue.svg "License MIT")
![Python 3.7.1](https://img.shields.io/badge/python-3.7.1-green.svg "Python 3")

# Meetings reporter

This module allows users to parse an input meetings file to find if there are conflicting ones.

## Installation

### Requirements

* Python >= 3.7.1
* pandas >= 1.3.5

### Installation

`pip install meetings-reporter`

## Usage

```
>>> from meetings_reporter import *
 
>>> report("FILE_PATH")
```

In order to get a coherent meetings report, make sure the input file has the format below:

```
start,end
8:15am,9:30am
9:00am,10:00am
2:30pm,4:00pm
```

### Example

The reporting of the file given above 

```
>>> from meetings_reporter import *
 
>>> report("/PATH_TO/ABOVE_FILE_NAME")
REPORT: 
 Conflict 1 :  08:15AM--->09:30AM  with  09:00AM--->10:00AM

```

## Author
+ Main maintainer: Mohamed Khalil Labidi (mklkun)