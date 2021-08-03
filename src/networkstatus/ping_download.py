#!/usr/bin/env python

import subprocess
import re
import pycurl


def ping(host, count):

    stats = dict()
    result = subprocess.Popen(('ping', '-f',  '-c', count, '-i', '.2', '-n', host),
                              stdout=subprocess.PIPE)
    output = subprocess.check_output(('tail', '-n', '2'), stdin=result.stdout)
    output = output.decode('utf-8')
    result.wait()

    print(output)
    loss = re.search(r'(\S+)% packet loss', output)
    stats['loss'] = loss.group(1)

    stats_m = re.search(r'= (\S+)/(\S+)/(\S+)/(\S+) ms', output)
    stats['min'] = stats_m.group(1)
    stats['avg'] = stats_m.group(2)
    stats['max'] = stats_m.group(3)
    stats['mdev'] = stats_m.group(4)

    print(stats)


def http(url):

    curl = pycurl.Curl()
    curl.setopt(curl.URL, "http://google.com/")
    curl.setopt(curl.VERBOSE, True)  # to see request details
    curl.perform()

    m = {}
    m['total-time'] = curl.getinfo(pycurl.TOTAL_TIME)
    m['namelookup-time'] = curl.getinfo(pycurl.NAMELOOKUP_TIME)
    m['connect-time'] = curl.getinfo(pycurl.CONNECT_TIME)
    m['pretransfer-time'] = curl.getinfo(pycurl.PRETRANSFER_TIME)
    m['redirect-time'] = curl.getinfo(pycurl.REDIRECT_TIME)
    m['starttransfer-time'] = curl.getinfo(pycurl.STARTTRANSFER_TIME)
    m['bytes'] = curl.getinfo(pycurl.SIZE_DOWNLOAD)
    m['speed'] = curl.getinfo(pycurl.SPEED_DOWNLOAD)

    print(m)

ping('1.1.1.1', '4')
http("")




