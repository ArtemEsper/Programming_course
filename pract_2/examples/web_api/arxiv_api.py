# https://github.com/metalcorebear/arXiv-parser
# https://github.com/samsinai/team_citation # https://sites.google.com/site/teamcitations/home-1
import urllib.request as libreq


with libreq.urlopen('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1') as url:
    r = url.read()
    print(r)