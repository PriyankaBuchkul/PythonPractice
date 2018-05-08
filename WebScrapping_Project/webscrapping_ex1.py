from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
      """
      Attempts to get the contents at 'url' by making an HTTP
      Get Request.If the content-type of responce is some kind of HTML/XML,
      return the text content,otherwise return None.
      """
      try:
            with closing(get(url,stream=True))as resp:
                  if is_good_response(resp):
                        return resp.content
                  else:
                        return None
      except RequestException as e:
            log_error('Error during request to {0}:{1}'.format(url,str(e)))
            return None

def is_good_response(resp):
      """
      returns True if the response seems to be htML otherwise
      """
      content_type=resp.headers['Content-Type'].lower()
      return (resp.status_code == 200
               and content_type is not None
               and content_type.find('html') > -1)

def log_error(e):
      """
       Its good idea to log errors.
       This function just prints them , but you can
       make it to do anything.
       """
      print(e)
