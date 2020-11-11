# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 21:00:54 2020

@author: bruno
"""
import os
import inspect

class Logger:
    #Logging levels:
    #Priority levels: Error>Warn>Info>Debug
    
    INFOLEVEL = "INFO"
    DEBUGLEVEL = "DEBUG"
    WARNLEVEL = "WARN"
    ERRORLEVEL = "ERROR"
    #NEWLEVEL = "NEWLEVEL"
    def __init__(self, level):
        self.level=level
        
    def Debug(self,msg):
        if self.level == self.DEBUGLEVEL :
            func_name = inspect.currentframe().f_back.f_code.co_name
            file_name = os.path.basename(__file__)
            print(f'[{self.level}][{file_name}][{func_name}] {msg}')  
    def Error(self,msg):#Logs on all levels
        func_name =inspect.currentframe().f_back.f_code.co_name
        file_name = os.path.basename(__file__)
        print(f'[{self.level}][{file_name}][{func_name}] {msg}')
    def Info(self,msg):
        if self.level != self.DEBUGLEVEL:
            func_name =inspect.currentframe().f_back.f_code.co_name
            file_name = os.path.basename(__file__)
            print(f'[{self.level}][{file_name}][{func_name}] {msg}')
    def Warn(self,msg):
        if self.level == self.WARNLEVEL or self.level == self.ERRORLEVEL: 
            func_name =inspect.currentframe().f_back.f_code.co_name
            file_name = os.path.basename(__file__)
            print(f'[{self.level}][{file_name}][{func_name}] {msg}')
    #def NEW level method


#%%Example

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
