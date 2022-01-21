# Hong Kong Chinese Name Converter

This project is a simple python programme that allows users to translate Chinese name to English name in HKID format

## Prerequisites
Before you begin, ensure you have met the following requirements :

Dependency | Versions
------------ | -------------
Python | 3.9
configparser | 5.2.0
et-xmlfile | 1.1.0
numpy | 1.22.1
openpyxl | 3.0.9
pandas | 1.3.5
python-dateutil | 2.8.2
pytz | 2021.3
six | 1.16.0
XlsxWriter | 3.0.2

## Usage

Create `config` folder to the exe programme directory

Modify the config file `config.ini`, move the config file to the config directory

`config.ini` Example
```
[DEFAULT]
# reference table data source, xlsx format
DATA_SOURCE_DIR=./config/
DATA_SOURCE_FILENAME=ChiName2Eng.xlsx

# Input data file, list the Chinese name line by line, TXT format
INPUT_FILE_DIR=./input/
INPUT_FILENAME=input.txt

# Output data file, xlsx format
OUTPUT_FILE_DIR=./output/
OUTPUT_FILENAME=output.xlsx

# Applcation log file, application will replace the <date> with today's date
PROGRAMME_LOG_DIR=./logs/
PROGRAMME_LOG_FILENAME=<date>.log
```

Prepare the reference file in xlsx format, seperate the Chinese word using "`,`"

Reference file example
English | Chinese
------------ | -------------
tze | 孜,止,芷,子,紫,致,字,祠,慈,梓,至
yat | 一,壹,溢,日,逸

Prepare the input data file in txt format, list the name line by line

Input data example:
```
許嘉能
陳苑一
馮子豪
王明
歐陽志成
```

Execute the programme and get the output file from output directory. An ',' will be added based on surname rule (After first word for the name containing 2-3 Chinese characters , after second word for the name containing 4 Chinese characters)

Output example:
English | Chinese
------------ | -------------
HUI, Ka Nung | 許嘉能
CHAN, Yuen Yat | 陳苑一
FUNG, Chi Ho | 馮子豪
WONG, Ming | 王明
AU YEUNG, Chi Shing | 歐陽志成

## Limitation
Since the committed reference table was taken form the internet, there might be translation problems. If necessary, the reference table can be modified pertaining to the requirement.

The programme now supports names with 2-4 Chinese characters

## Reference
I got the reference table from [here](
https://www.wikiwand.com/zh-hk/%E9%A6%99%E6%B8%AF%E6%94%BF%E5%BA%9C%E7%B2%B5%E8%AA%9E%E6%8B%BC%E9%9F%B3)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Changelog
[1.0.0] - 2022-01-18

###
- Initial commit
- Added README file