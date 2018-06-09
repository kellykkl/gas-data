# gas-data

This script takes monthly gas flow data for Apr 2018 and May 2018 from http://www.interconnector.com/operational-data/historical-data/data-downloads/ and returns a cleaned dataframe.

## Installation 
First ensure that that the following libraries are installed in your machine:
* pandas
* numpy
* pytz

Then download this repository as a zip file and unzip it. In the command line, navigate to the folder that contains setup.py, and run the following command:

```pip install .```

## Usage
In the command line, run `python`, then `import gas_data`, and finally get the data frame using `gas_data.getdf()`.
