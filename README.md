# PMG_Challenge
## Coding assessment for PMG as part of interview process for GLP. Original repo can be found at https://github.com/AgencyPMG/ProgrammingChallenges/tree/master/csv-combiner.

I did have to change one of the CSV files - clothing.csv. Some of the categories for the rows were written as "\"Gingham\" Shorts". To make this match the rest of the example csv files given, I changed those categories to "Gingham Shorts". 

I wrote the code on Visual Studio Code and the version of Python used was Python 3.10.9. 

Shown below is an example of how the code was executed via command line.
```
python main.py ./fixtures/accessories.csv ./fixtures/clothing.csv > output.csv
```

For testing, combinations are as followed
* output1.csv is accessories.csv and clothing.csv
* output2.csv is accessories.csv and household_cleaners.csv
* output3.csv is clothing.csv and household_cleaners.csv
* output4.csv is accessories.csv, clothing.csv, and household_cleaners.csv
