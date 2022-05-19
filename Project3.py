# File: Project3.py
# Student: Harini Shanmugam
# UT EID: hs28663
# Course Name: CS303E
#
# Date Created: 11/29/21
# Date Last Modified: 12/1/21
# Description of Program: This program will allow the user to input queries about the populations of Texas county names
# and retrieve the corresponding information from a database given to us in the csv file.

import os.path


# Part One: Read lines from the input file. Create two data structures (dictionary and list of county names)
def census(dictionary, listOfNames):
    data = open("populationdata.csv", "r")


# Part Two: Query processing functionality
def main():
    if not os.path.isfile("populationdata.csv"):
        return "File does not exist"
    else:
        print()
        s = {}
        counties = []
        census(s, counties)

        print("Welcome to the Texas Population Dashboard. \n"
              "This provides census data from the 2010 census and \n"
              "estimated population data in Texas as of 1/1/2020.")
        print()
        print("Creating dictionary from file: populationdata.csv")
        print()
        print("Enter any of the following commands: \n"
              "\033[1mHelp\033[0m - list available commands; \n"
              "\033[1mQuit\033[0m - exit this dashboard; \n"
              "\033[1mCounties\033[0m - list all Texas counties; \n"
              "\033[1mCensus <countyName>/Texas\033[0m - population in 2010 census by specified county or statewide; \n"
              "\033[1mEstimated <countyName>/Texas\033[0m - estimated population in 2020 by specified county or "
              "statewide; \n"
              "\033[1mGrowth <countyName>/Texas\033[0m - percent change from 2010 to 2020, by county or statewide.")
        print()

        commandInput = str(input("\033[1mPlease enter a command: \033[0m"))
        commandInputLowered = commandInput.lower()

        while True:
            if commandInputLowered == "help":
                print("Enter any of the following commands: \n"
                      "\033[1mHelp\033[0m - list available commands; \n"
                      "\033[1mQuit\033[0m - exit this dashboard; \n"
                      "\033[1mCounties\033[0m - list all Texas counties; \n"
                      "\033[1mCensus <countyName>/Texas\033[0m - population in 2010 census by specified county or "
                      "statewide; \n"
                      "\033[1mEstimated <countyName>/Texas\033[0m - estimated population in 2020 by specified county "
                      "or statewide; \n"
                      "\033[1mGrowth <countyName>/Texas\033[0m - percent change from 2010 to 2020, by county or "
                      "statewide.")
            elif commandInputLowered == "quit":
                print("Thank you for using the Texas Population Database Dashboard.  Goodbye!")
                break
            elif commandInputLowered == "counties":
                for i in range(0, len(counties)):
                    if i != 0 and i % 10 == 0:
                        print("\n" + counties[i].title() + ",", end="")
                    else:
                        print(counties[i].title() + ",", end=" ")
                print("\n")
            elif commandInputLowered == "census":
                print(commandInputLowered.title(), "county had", "DATA", "citizens in the 2010 Census.")
                if commandInputLowered == "census texas":
                    print("Texas total population in the 2010 Census: 21145565 ")
                else:
                    print("County", commandInputLowered.title(), "is not recognized.")
            elif commandInputLowered == "estimated":
                print(commandInputLowered.title(), "county had estimated population (January, 2020):", "DATA")
                if commandInputLowered == "estimated texas":
                    print("Texas estimated population (January, 2020): 33140640")
                else:
                    print("County", commandInputLowered.title(), "is not recognized.")
            elif commandInputLowered == "growth":
                print("County", commandInputLowered.title(), "had percent population change (2010 to 2020):", "DATA")
                if commandInputLowered == "growth texas":
                    print("Texas had percent population change (2010 to 2020): 56.73%")
                else:
                    print("County", commandInputLowered.title(), "is not recognized.")
            else:
                print("Command is not recognized.  Try again!")

            print("")
            commandInput = str(input("\033[1mPlease enter a command: \033[0m"))
            commandInputLowered = commandInput.lower()
