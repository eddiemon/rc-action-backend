#!/usr/bin/env bash
scrapy crawl TweetScraper -a query="danger OR terrorist OR emergency OR disaster OR conflict since:2019-10-25 until:2019-11-03 near:Stockholm"
