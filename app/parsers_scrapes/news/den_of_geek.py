"""File containing parsing method for den of geek"""
from typing import AnyStr

import feedparser
from slack import WebClient

from app.parsers_scrapes.news.constants import DEN_OF_GEEK_RSS_FEED
from app.parsers_scrapes.news.utils import send_heading, \
                                           send_response


def get_top_10_dog(slack_client: WebClient,
                   channel: AnyStr = "#ideas") -> None:
    """
    This method fetches top 10 news articles and sends them as links
    To the specified channel
    :param slack_client: WebClient
    :param channel: Channel to post content on
    :return: None
    """
    parsed_data = feedparser.parse(DEN_OF_GEEK_RSS_FEED)
    if len(parsed_data):
        send_heading(slack_client, channel, "Den of Geek")
        send_response(slack_client, channel, parsed_data["entries"])