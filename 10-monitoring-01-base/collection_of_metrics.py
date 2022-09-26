#!/usr/bin/python3

import datetime, time
import os

def write_to_file(filename, data):
  with open(f'/tmp/{filename}', 'a+') as f:
    f.write(f'{data}\n')


def main():
  date = datetime.datetime.now().strftime("%Y-%m-%d")
  filename = f'{date}-awesome-monitoring.log'
  metrics_time = int(time.time())
  write_to_file(filename, metrics_time)
  mertics = os.system(f"cat /proc/loadavg /proc/uptime /proc/swaps >> /tmp/{filename}")

if __name__ == '__main__':
    main()
