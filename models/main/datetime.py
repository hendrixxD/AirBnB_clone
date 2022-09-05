#!/usr/bin/python3

from datetime import datetime

def curent_time():
    """using string format"""
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%dT%H:%M:%S.%f")
    return current_time

    """using isoformat"""
    time_now = datetime.now().isoformat()
    return time_now

    """datetime in utc"""
    live_time = datetime.utcnow()
    return live__time


def main():
    current_time()
main()
