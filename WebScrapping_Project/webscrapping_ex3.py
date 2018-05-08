#how many times the name is searched
from webscrapping_ex1 import *
from bs4 import BeautifulSoup

def get_hits_on_name(name):
      """
      Accepts a 'name' of a mathematicians  and retrurns the
      number of hits that mathematicians's wikipidea page received
      in the last 60 days , as an 'int'
      """
      #url_root is a template string that used to buld the url
      url_root='https://xtools.wmflabs.org/articleinfor/en.wikipedia.org/{}'
      response=simple_get(url_root.format(name))

      if response is not None:
            html=BeautifulSoup(response,'html.parser')
            hit_link=[a for a in html.select('a')
                      if a['href'].find('latest-60')>-1]
            if len(hit_link) > 0:
                  #strip commas
                  link_text=hot_link[0].text.replace(',','')
                  try:
                        #convert to integer
                        return int(link_text)
                  except:
                        log_error("could's parse {} as in 'int'".format(link_text))
      log_error('No pageviews found for {}:'.format(name))
      return None




#print(get_hits_on_name('Isaac Newton'))

            
            
