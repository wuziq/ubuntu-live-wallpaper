# title           :WallpaperManager
# description     :This scripts contains wallpaper manipulation functions
# author          :Saddam H
# date            :2016-10-30
# version         :0.1
# usage           :from WallpaperManager import *
# notes           :Follow me @thedevsaddam
# python_version  :2.6.6
# ==============================================================================

import os
import random
import urllib

from helper import base_path, log, download_image
from configManager import get_categories, get_tags


def download_wallpaper(width=1920, height=1080):
    """Return the downloaded wallpaper file name"""

    # available categories
    categories = get_categories()
    category = random.choice(categories)

    # image url
    base_url = "https://source.unsplash.com"
    tags = get_tags()
	collection = 1598183
    #image_url = '{}/{}x{}?{},{}'.format(base_url,
    #                                    str(width), str(height), category, tags)
    image_url = '{}/{}/{}/{}x{}'.format(base_url, "collection", str(collection), str(width), str(height))
    #image_url = "https://source.unsplash.com/collection/1598187/1920x1080"
    # landscapes
    #image_url = "https://source.unsplash.com/collection/1598189/1920x1080"
    # my first collection (everything)
    #image_url = "https://source.unsplash.com/collection/1598183/1920x1080"

    # download image
    try:
        wallpaper_name = 'wallpaper.jpg'
        response = download_image(image_url, base_path("/" + wallpaper_name))
    except:
        # if previously download wallpaper not exist
        if not os.path.isfile(base_path("/" + wallpaper_name)):
            wallpaper_name = "default-wallpaper.jpg"  # show the default wallpaper
        log('Unable to download wallpaper')

    return base_path("/" + wallpaper_name)


def set_wallpaper(file_name):
    """Set wallpaper"""
    dbus_session_bus_address = "PID=$(pgrep gnome-session) && export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$PID/environ|cut -d= -f2-) && "
    command = "{}gsettings set org.gnome.desktop.background picture-uri file:///{}".format(
        dbus_session_bus_address, file_name)

    os.system(command)
