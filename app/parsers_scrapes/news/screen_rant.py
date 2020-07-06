"""File containing method for parsing screen rant"""
from typing import AnyStr

import feedparser

from app.parsers_scrapes.news.constants import SCREEN_RANT_RSS_FEED, \
                                               FEEDPARSER_AGENT
from app.parsers_scrapes.news.utils import send_heading, \
                                           send_response
from app.utils import get_slack_client


def get_screen_rant_news(slack_signing_key: AnyStr,
                         channel: AnyStr = "#ideas") -> None:
    """
    This method fetches top 100 news items from ScreenRant RSS Feed
    :param slack_signing_key: Signing key from config
    :param channel: Channel to post content on
    :return: None
    """
    slack_client = get_slack_client(slack_signing_key)

    parsed_data = feedparser.parse(SCREEN_RANT_RSS_FEED,
                                   agent=FEEDPARSER_AGENT)

    if len(parsed_data['entries']):
        send_heading(slack_client, channel, "Screen Rant")
        send_response(slack_client, channel, parsed_data["entries"])
