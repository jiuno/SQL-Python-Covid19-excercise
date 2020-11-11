# Sirena-Assignment
Bruno Fernando Alliani

## Contents
This repository contains 8 files. 
* ```SQL_Postgresql_Sirena.sql```
* ```Logger_Sirena.py```
* ```Covid_regions_Sirena.py```
* ```Lockdown strategies and curve death profiles.pptx```
* ``` 3_lockdown.svg ```
* ``` Europa.svg ```
* ``` LAT.svg ```
* ``` Asia.svg ````

## Databases SQL (PostgreSQL)
The three excercises are inside the ```SQL_Postgresql_Sirena.sql``` file.
I tested my queries on a mock dataset. This mock dataset included the tables provided in the ERD.

## Python Classes
The Logger object has 4 logging methods available (Error, Warn,Info,Debug) with different behaviour based on 4 different levels (ERROR,WARN,INFO,DEBUG). The order of relevance is as follows:
ERROR>WARN>INFO>DEBUG.  

Behaviour of Logger on different levels:
* Error Level: Prints all logs.
* Warn  Level: Prints all error and warning logs.
* Info  Level: Prints all logs except DEBUG logs.
* DEBUG Level: Prints only debug logs.

### Example
```Python
#Enviromental variables for setting the logger level.
loggerLevel = {
    "Production":Logger.WARNLEVEL,
    "Staging":Logger.INFOLEVEL,
    "Development":Logger.DEBUGLEVEL
    }
#Get enviromental variable
scope = os.environ['SCOPE']

#Sets the level for the logger using the env variable
logger = Logger(loggerLevel[scope])

def Calculate(a,b):
    result = a+b
    logger.Debug("The result of a+b is "+str(result))
    result = result * result
    logger.Debug("The result of squaring result is "+str(result))
    result = result + 10
    logger.Debug("The result of adding 10 to the result is "+str(result))
    try:
        result = result / b
    except Exception as e:
        logger.Error(str(e))
        logger.Warn("You can't divide by zero!")
    return result
        
resultado=Calculate(1,0)
logger.Info("The result of Calculate is "+str(resultado))
```

## Data Analysis
I've spent most of the time doing an exploratoy analysis on the data. The database provided contained updated confirmed, recovered* and death cases based primarily on the COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University https://github.com/CSSEGISandData/COVID-19#covid-19-data-repository-by-the-center-for-systems-science-and-engineering-csse-at-johns-hopkins-university. I used the API provided for creating the plots in the PowerPoint presentation. It still needs a lot of exploration yet to form a solid hypothesis. I am aware it is not a solid hypothesis yet.


