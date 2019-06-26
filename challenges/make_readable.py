



def make_readable(seconds):
    if seconds > 359999:
        return "Maximum is: 359,999 seconds"
    sec =int((seconds % 3600) % 60)
    min = int(((seconds % 3600 ) - sec)/60)
    hour = int((seconds - (seconds % 3600))/3600)
    return ('{0:02d}:'.format(hour) + '{0:02d}:'.format(min) +'{0:02d}'.format(sec))


print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))