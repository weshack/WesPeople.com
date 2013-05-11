from scrapy.spider import BaseSpider
from scrapy.http import FormRequest
from scrapy.http.request import Request
from scrapy.selector import HtmlXPathSelector
from scrapy import log
from wesconnect.items import Alum

# import login credentials
from wesconnect.creds import *

class WesConnectSpider(BaseSpider):
  name = "wesconnect"
  allowed_domains = ["wesleyan.edu", "securelb.imodules.com"]
  start_urls = [
      "https://securelb.imodules.com/s/1318/index.aspx?sid=1318&gid=1&pgid=3&cid=40"
      ]

  def parse(self, response):
    # If we're logged out, login
    if "Login/Logout" in response.body:
      # find viewstate and eventsate
      x = HtmlXPathSelector(response)
      viewstate = x.select("//input[@name='__VIEWSTATE']").select('@value').extract()[0]
      eventvalidation = x.select("//input[@name='__EVENTVALIDATION']").select('@value').extract()[0]

      return [FormRequest(url="https://securelb.imodules.com/s/1318/index.aspx?sid=1318&gid=1&pgid=3&cid=40",
        formdata = {
          '__EVENTTARGET' : '',
          '__EVENTARGUMENT' : '',
          '__VIEWSTATE' : viewstate,
          '__EVENTVALIDATION' : eventvalidation,
          'quicklinks' : '',
          'cid_40$txtUsername' : WESCONNECT_USERNAME,
          'cid_40$txtPassword' : WESCONNECT_PASSWORD,
          'cid_40$btnLogin' : "Login"
          },
        callback=self.parse)]
    else:
      # We are logged in
      print "We're logged in, go to directory page"
      return Request("http://wesconnect.wesleyan.edu/directory",
                     callback=self.directory_parser)


  def directory_parser(self, response):
    """
    Given a http://wesconnect.wesleyan.edu/directory search form, search and
    parse.
    """
    print "On a directory page, sending serach data"


    if "<b>Search Operator&nbsp;/&nbsp;Search Value</b>" in response.body:
      print "This page has a search form"

      x = HtmlXPathSelector(response)
      viewstate = x.select("//input[@name='__VIEWSTATE']").select('@value').extract()[0]
      eventvalidation = x.select("//input[@name='__EVENTVALIDATION']").select('@value').extract()[0]

      for year in xrange(1950, 2013):
        year = str(year)

        yield FormRequest.from_response(response,
          formdata = {
            # LastName Comparison method
            #'cid_41$SearchGUI$sc285$ddComparison_285' : "Contains",
            #'cid_41$SearchGUI$sc285$mf_285' : last_name,

            # FirstName Comparison method
            #'cid_41$SearchGUI$sc284$ddComparison_284' : "Contains",
            #'cid_41$SearchGUI$sc284$mf_284' : "",

            ## Year should be filled in or non-existant, NEVER blank
            'cid_41$SearchGUI$sc36$mf_36' : year,
            },
          callback=self.listing_parser)
    else:
      print "This is a result from a search"

      from scrapy.shell import inspect_response
      inspect_response(response)
      print "Got to results listing"


  def listing_parser(self, response):
    """
    Given a paginated listing of alumni, parse members and reparse individual page and rerun on next
    pages
    """
    # Get all pages
    x = HtmlXPathSelector(response)

    # if has numbered responses
    pages_hrefs = [i.extract().split("'")[1] for i in x.select("//div[contains(@class,'rgNumPart')]/a/@href")]
    pages = x.select("//div[contains(@class,'rgNumPart')]/a")

    requests = []

    # if the first link is a previous pages, delete it
    if "Previous Pages" in pages[0].extract():
      del pages_hrefs[0]

    # if next pages, pop and rerun listing_parser on it
    if "Next Pages" in pages[-1].extract():
      requests.append(FormRequest.from_response(response,
          formdata = {'__EVENTTARGET' : pages_hrefs.pop(), },
          callback=self.listing_parser))

    # parse each page including the first with scraper
    for href in pages_hrefs:
      requests.append(FormRequest.from_response(response,
          formdata = {'__EVENTTARGET' : href, },
          callback=self.listing_scraper))

    return requests

  def listing_scraper(self, response):
    """
    Given a page with members, scrape user info
    """
    # Get member info
    x = HtmlXPathSelector(response)

    reqs = []

    for alum_tr in x.select("//table[@id='cid_41_RadGrid1_ctl00']/tbody/tr"):
      tds = alum_tr.select("td")


      if len(tds[1].select("a/@href").extract()) == 0:
        print "GOT A WEIRD RESPONSE WITH BLANK NAMES, handling"
        alum = Alum(
          mid = tds[0].select("text()").extract(),
          #name = tds[1].select("a/text()").extract(),
          preferred_class_year = tds[2].select("text()").extract(),
          city = tds[3].select("text()").extract(),
          state = tds[4].select("text()").extract(),
          page_url =
          "http://wesconnect.wesleyan.edu/s/1318/index.aspx?sid=1318&gid=1&pgid=94&cid=256&mid=" +
          tds[0].select("text()").extract()[0],
          country = tds[5].select("text()").extract()
        )
        req = Request(url = alum['page_url'], callback=self.member_parser)
        req.meta['item'] = alum
        reqs.append(req)
      else:
        alum = Alum(
          page_url = "http://wesconnect.wesleyan.edu" + tds[1].select("a/@href").extract()[0],
          mid = tds[0].select("text()").extract(),
          name = tds[1].select("a/text()").extract(),
          preferred_class_year = tds[2].select("text()").extract(),
          city = tds[3].select("text()").extract(),
          state = tds[4].select("text()").extract(),
          country = tds[5].select("text()").extract()
        )
        req = Request(url = alum['page_url'], callback=self.member_parser)
        req.meta['item'] = alum
        reqs.append(req)

    return reqs

  def member_parser(self, response):
    """
    Given a single members page and a response with an already half created
    Alum item, update the rest of the Alum data and yield the item back
    """
    alum = response.request.meta['item']
    x = HtmlXPathSelector(response)

    #educ info
    for tr in x.select("//div[@id='cid_256$ctl00$ctl01$RichPanel_949_ContentDiv']//tr"):
      field = tr.select("td/text()")[0].extract()

      try:
        value = tr.select("td/text()")[1].extract()
      except IndexError:
        # probably a link in one of the fields
        value = tr.select("td")[1].select("a/text()").extract()

      if field == "Wesleyan Degree School 1 :":
        alum['wesleyan_degree_school_1'] = value
      if field == "Wesleyan Degree Year 1:":
        alum['wesleyan_degree_year_1'] = value
      if field == "Wesleyan Degree 1:":
        alum['wesleyan_degree_1'] = value
      if field == "Wesleyan Degree 1 Major 1:":
        alum['wesleyan_degree_1_major_1'] = value
      if field == "Wesleyan Degree 1 Major 2:":
        alum['wesleyan_degree_1_major_2'] = value
      if field == "Wesleyan Degree 1 Major 3:":
        alum['wesleyan_degree_1_major_3'] = value

    #member info
    for tr in x.select("//div[@id='cid_256$ctl00$ctl01$RichPanel_1670_ContentDiv']//tr"):

      field = tr.select("td/text()")[0].extract()
      try:
        value = tr.select("td/text()")[1].extract()
      except IndexError:
        # probably have a link in the name somewhere
        value = tr.select("td")[1].select("a/text()").extract()

      if field == "First Name:":
        alum['first_name'] = value
      if field == "Nickname:":
        alum['nickname'] = value
      if field == "Last Name at Graduation:":
        alum['last_name_at_grad'] = value
      if field == "Last Name:":
        alum['last_name'] = value
      if field == "Preferred Class Year:":
        alum['preferred_class_year'] = value
      if field == "Preferred E-mail:":
        alum['preferred_email'] = value

    #employment info
    for tr in x.select("//div[@id='cid_256$ctl00$ctl01$RichPanel_950_ContentDiv']//tr"):

      field = tr.select("td/text()").extract()[0]
      try:
        value = tr.select("td/text()")[1].extract()
      except IndexError:
        # probably have a link in the name somewhere
        value = tr.select("td")[1].select("a/text()").extract()

      if field == "Company Name:":
        alum['company_name'] = value
      if field == "Position/Title:":
        alum['position_title'] = value
      if field == "Position Status:":
        alum['position_status'] = value
      if field == "Business Address 1:":
        alum['business_address_1'] = value
      if field == "Business Address 2:":
        alum['business_address_2'] = value
      if field == "Business Address City:":
        alum['business_address_city'] = value
      if field == "Business Address State:":
        alum['business_address_state'] = value
      if field == "Business Address Zip:":
        alum['business_address_zip'] = value
      if field == "Business Address Country:":
        alum['business_address_country'] = value
      if field == "Occupation:":
        alum['occupation'] = value
      if field == "Industry:":
        alum['industry'] = value

    yield alum
