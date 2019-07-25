# Speedtest InfluxDB
Log your internet speeds to Influx DB.
The script currently logs download and upload speeds (in b/s) and ping to influx db.

The data written to the database looks like this:
```
> SELECT * FROM internetSpeed
name: internetSpeed
time                download           ping  upload
----                --------           ----  ------
1564068380338827008 24137205.190151006 7.247 4999612.83820897
1564069140744026880 21963406.450794857 7.343 4603067.451408845
1564069272956461824 24177880.030567713 7.404 4936487.407350518
```

## Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.  
This project uses [pipenv](https://github.com/pypa/pipenv) to manage it's dependencies.

### Prerequisites
* Python 3.7
* pipenv
  * Install with `pip install pipenv`

### Installing
1. Run `pipenv install`
2. Done

### Edit the config
1. Copy example config `cp config.example.json config.json`
2. Fill in all values

### Run the script
```
$ pipenv run ./speedtest-influxdb.py
```

## Built with
* Python
* `speedtest-cli`
* `influxdb`
