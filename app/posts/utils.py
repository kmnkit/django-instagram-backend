# -*- coding: utf-8 -*-
import re


def save_hashtags(desc):
    hashtags = re.compile("#[가-힣|a-z|A-Z|0-9]+").findall(desc)
    hashtags = [f"#{tag[1:].capitalize()}" for tag in hashtags]
    hashtags = list(set(hashtags))
    return hashtags
