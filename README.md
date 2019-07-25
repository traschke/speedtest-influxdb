# Speedtest InfluxDB
Log your internet speeds to Influx DB.

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
