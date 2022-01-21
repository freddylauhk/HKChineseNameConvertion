from multiprocessing.connection import wait
import os
import pandas as pd
import xlsxwriter
import configparser
import logging
from datetime import date
import time

# Read config
config = configparser.ConfigParser()
config.read('./config/config.ini')

DATA_SOURCE_DIR = config['DEFAULT']['DATA_SOURCE_DIR']
DATA_SOURCE_FILENAME = config['DEFAULT']['DATA_SOURCE_FILENAME']
INPUT_FILE_DIR = config['DEFAULT']['INPUT_FILE_DIR']
INPUT_FILENAME = config['DEFAULT']['INPUT_FILENAME']
OUTPUT_FILE_DIR = config['DEFAULT']['OUTPUT_FILE_DIR']
OUTPUT_FILENAME = config['DEFAULT']['OUTPUT_FILENAME']
PROGRAMME_LOG_DIR = config['DEFAULT']['PROGRAMME_LOG_DIR']
PROGRAMME_LOG_FILENAME = config['DEFAULT']['PROGRAMME_LOG_FILENAME'].replace(
    "<date>", date.today().strftime("%Y%m%d"))

# Check directory exists
if not os.path.exists(DATA_SOURCE_DIR):
    os.makedirs(DATA_SOURCE_DIR)
    print("%s created" % DATA_SOURCE_DIR)
if not os.path.exists(INPUT_FILE_DIR):
    os.makedirs(INPUT_FILE_DIR)
    print("%s created" % INPUT_FILE_DIR)
if not os.path.exists(OUTPUT_FILE_DIR):
    os.makedirs(OUTPUT_FILE_DIR)
    print("%s created" % OUTPUT_FILE_DIR)
if not os.path.exists(PROGRAMME_LOG_DIR):
    os.makedirs(PROGRAMME_LOG_DIR)
    print("%s created" % PROGRAMME_LOG_DIR)

# Set python logging
logging.basicConfig(level=logging.NOTSET,
                    format='%(asctime)s %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    handlers=[logging.FileHandler(os.path.join(PROGRAMME_LOG_DIR, PROGRAMME_LOG_FILENAME), 'a', 'utf-8')])


logger = logging.getLogger("chinameconvert")
logger.debug("Logger config done")

# Read data file and split to searching list


def readRefFile():
    logger.debug("Reading reference file : %s", os.path.join(
        DATA_SOURCE_DIR, DATA_SOURCE_FILENAME))

    try:
        data = pd.read_excel(os.path.join(
            DATA_SOURCE_DIR, DATA_SOURCE_FILENAME))
        df = pd.DataFrame(data, columns=['English', 'Chinese'])

        df_list = df.values.tolist()
        for data in df_list:
            data[1] = data[1].split(',')
    except:
        logger.exception("Error occurred when reading reference file")

    logger.debug("Reading reference file - Completed")

    return df_list

# Lookup the English translation from reference list
# Return "?" if lookup failed
def findEngName(referenceList, chiword):
    for reference in referenceList:
        if(chiword in reference[1]):
            return reference[0]

    return "?"


def main():
    logger.debug("------------------- Name Convertion Programme Start -------------------")

    refList = readRefFile()
    workbook = xlsxwriter.Workbook(os.path.join(OUTPUT_FILE_DIR, OUTPUT_FILENAME))
    worksheet = workbook.add_worksheet()

    inputFile = open(os.path.join(INPUT_FILE_DIR, INPUT_FILENAME), 'r', encoding="utf-8")
    Lines = inputFile.readlines()

    cell_format = workbook.add_format()
    cell_format.set_bold()

    worksheet.write(0, 0, "English", cell_format)
    worksheet.write(0, 1, "Chinese", cell_format)

    count = 1

    for line in Lines:
        line = line.strip()
        logger.debug("Chinese Name : %s", line)
        result = ""
        wordcount = 0
        for word in line:
            tempword = findEngName(refList, word)

            if(wordcount <= int(len(line)/2) - 1):
                result += tempword.upper()
                if(wordcount == int(len(line)/2) - 1):
                    result += ", "
                else:
                    result += " "
            else:
                result += tempword.capitalize() + " "

            wordcount += 1

        logger.debug("Converted English Name : %s", result.strip())
        worksheet.write(count, 0, result.strip())
        worksheet.write(count, 1, line.strip())

        count += 1

    inputFile.close()
    workbook.close()

    logger.debug("------------------- Name Convertion Programme End -------------------")


main()
