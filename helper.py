# title           :helper
# description     :Contains some essential helper functions
# author          :Saddam H
# date            :2016-11-01
# version         :0.1
# usage           :import from helper *
# notes           :Follow me @thedevsaddam
# python_version  :2.6.6
# ==============================================================================

# Import essential libraries
import os
import sys
import datetime

if sys.version_info[0] < 3:
    import urllib
else:
    import urllib.request


def base_path(path=''):
    """Return base directory path"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path + path


def get_max(list_of_string):
    """Return maximum value from a list of string or integer """
    return max(map(int, list_of_string))


def get_window_size():
    """Return the window width and height"""
    width = os.popen(
        "xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f1").read().strip(
        "\n")
    height = os.popen(
        "xrandr --current | grep '*' | uniq | awk '{print $1}' | cut -d 'x' -f2").read().strip(
        "\n")
    if '\n' in width:
        widths = width.split('\n')
        heights = height.split('\n')
        return widths, heights
    else:
        return width, height


def get_max_window_size():
    """Return maximum resolution of connected monitors"""
    window_sizes = list(get_window_size())
    widths = []
    heights = []

    if isinstance(window_sizes[0], (list, tuple)):
        for window_size in window_sizes[0]:
            widths.append(window_size)

        for window_size in window_sizes[1]:
            heights.append(window_size)

        width = get_max(widths)
        height = get_max(heights)
    else:
        width = int(window_sizes[0])
        height = int(window_sizes[1])

    return width, height


def log(message, level='DEBUG'):
    """write a custom log"""
    try:
        log_file = base_path('/ubuntu-live-wallpaper.log')

        with open(log_file, 'a') as file_handler:
            # if log file is greater 5mb then remove
            if os.path.getsize(log_file) > 5000000:
                os.remove(log_file)
            file_handler.write(
                str(level) + " -> [" + str(datetime.datetime.now()) + "]: " + str(message) + "\n")
    except:
        pass


def download_image(image_url, file_name):
    """Download image from url"""
    if sys.version_info[0] < 3:
        response = urllib.urlretrieve(image_url, file_name)
    else:
        response = urllib.request.urlretrieve(image_url, file_name)

    return response
