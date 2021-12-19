from scraping import ScrapingClient

scrapingClient = ScrapingClient()

try:
  scrapingClient.api.update_status(scrapingClient.scraping())
except Exception as e:
  print(e)
  raise e