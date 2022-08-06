from datetime import datetime

# (t, timestamp, style)
time_tag_builder = '<{t}:{timestamp}:{style}>'.format

def timestamp(dt: datetime):
    return int(dt)
# key:value
displayFormats = {
    't': "LT",  # short time
    'T': "LTS",  # long time
    'd': "L",  # short date
    'D': "LL",  # long date
    'f': "LLL",  # short date/time
    'F': "LLLL",  # long date/time
    "R": "R"  # relative time
}

formatsExplaination = {
't': 'short time',
'T': 'long time',
'd': 'short date',
'D': 'long date',
'f': 'short date/time',
'F': 'long date/time',
"R": 'relative time',
}

if __name__ == '__main__':
    timestamp = int(datetime.now().timestamp())
    for k, v in formatsExplaination.items():
        print(v, time_tag_builder(t='t', timestamp=timestamp, style=k))
