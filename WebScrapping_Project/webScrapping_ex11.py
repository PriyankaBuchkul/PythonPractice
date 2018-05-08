from webScrapping_ex10 import simple_get
from bs4 import BeautifulSoup
##raw_html = simple_get('http://www.fabpedigree.com/james/mathmen.htm')
##print(len(raw_html))
##html = BeautifulSoup(raw_html, 'html.parser')
##no_html = simple_get('https://realpython.com/blog/nope-not-gonna-find-it')
##for i, li in enumerate(html.select('li')):
##    print(i, li.text)

def get_names():
    """
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician
    """
    url = 'http://www.fabpedigree.com/james/mathmen.htm'
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        names = set()
        for li in html.select('li'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
        return list(names)

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))

