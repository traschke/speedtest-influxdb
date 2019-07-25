#!/usr/bin/env python3

import speedtest
from influxdb import InfluxDBClient
from datetime import datetime
import pytz
import json

def take_speedtest():
    servers = []
    threads = None

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()

    return s.results.dict()

def generate_influxdb_points(time, download, upload, ping):
    data = [
        {
            "measurement": "internetSpeed",
            "tags": {

            },
            "time": time,
            "fields": {
                "download": download,
                "upload": upload,
                "ping": ping
            }
        }
    ]
    return data

def write_points_to_influx_db(host, port, username, password, database, points):
    client = InfluxDBClient(host=host, port=port, username=username, password=password)
    client.switch_database(database)
    client.write_points(points)

def read_config():
    with open('config.json') as json_data_file:
        config = json.load(json_data_file)

    return config

def main():
    config = read_config()
    influx_conf = config['influxdb']

    now_utc = datetime.now().astimezone(pytz.utc)

    speedtest_results = take_speedtest()

    points = generate_influxdb_points(now_utc.isoformat(), speedtest_results['download'], speedtest_results['upload'], speedtest_results['ping'])

    write_points_to_influx_db(influx_conf['host'], influx_conf['port'], influx_conf['username'], influx_conf['password'], influx_conf['database'], points)

if __name__ == "__main__":
    main()
