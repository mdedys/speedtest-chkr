import csv
from datetime import datetime
import logging
import speedtest
import time

logger = logging.getLogger(__name__)

servers = []
threads = 1

filename = "./data/speedtest_results.csv"

headers = ["date", "time", "download", "upload", "ping", "server_url", "server_name", "server_country"]


def to_mbps(bits):
    return round(bits / 1000000, 2)


def main():

    logger.info("Creating CSV file to track data")

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()

    s = speedtest.Speedtest()

    while True:
        logger.info("Running Speedtest")
        s.get_servers(servers)
        s.get_best_server()
        s.download(threads=threads)
        s.upload(threads=threads)

        logger.info("Logging Results")
        results = s.results.dict()

        download = results.get("download", 0)
        upload = results.get("upload", 0)
        ping = results.get("ping")
        server = results.get("server")

        with open(filename, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writerow({
                "date": datetime.today().strftime("%Y-%m-%d"),
                "time": datetime.today().strftime("%H:%M:%S"),
                "download": to_mbps(download),
                "upload": to_mbps(upload),
                "ping": ping,
                "server_url": server.get("url", ""),
                "server_name": server.get("name", ""),
                "server_country": server.get("country", "")
            })
        logger.info("Sleeping for 30 minutes")
        time.sleep(1800)


if __name__ == "__main__":
    main()
