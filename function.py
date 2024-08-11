from pydantic import Field
from instructor import OpenAISchema
import constants
import difflib
import requests
from typing import Union





class GetOpenQData(OpenAISchema):
    """
    Extract the topic from user query 
    """
    topic: str = Field(..., description="The topic of user query")
    results: str = Field(description="The real information you should use to generate a response, take step by step to answer correctly")

    def run(self):
      self.results = call_api(liteBestMatch(self.topic))
      print(self.results)

      return(f"the query topic is {self.topic} and results you will use is {self.results}")
    
class Fetch(GetOpenQData):
    """call external API based topic."""
    jsonData: str = Field(description="retrieve data from calling API")

    def run(self):
        """Process the fetch action."""
        return f"fetch data as json format: {self.jsonData}"

class finish(GetOpenQData):
    """ Generate and insight from json data you have and finish """

    def run(self):
        """Finish and generate answer."""
       
        return f"your answer is based on: {self.results}"



# get best match to reformat dataset_id to feed Base URl 

def liteBestMatch(query):
   lst =  ["weekly-real-estate-newsletter","qatar-monthly-statistics-total-population-of-2022","qatar-monthly-statistics-population-by-gender", 
        "qatar-monthly-statistics-population-by-gender", "qms-commercial-banks-deposits", "qatar-monthly-statistics-new-driving-licenses",
         "qms-live-births-by-gender", "qatar-monthly-statistics-hotel-occupancy-rate-2022","qms-hotel-average-room-rate",
          "qatar-monthly-statistics-revenue-per-available-room","qms-average-room-rate","qatar-monthly-statistics-sewage-water","qatar-monthly-statistics-total-water-production","qatar-monthly-statistics-water-consumption", "qms-climate-2022"
          ,"qatar-monthly-statistics-registered-new-vehicle","qatar-monthly-statistics-traffic-violations","qms-arriving-vessels-movements","qatar-monthly-statisticsvisitor-arrivals-by-mode-of-entry",
          "number-of-sold-properties-by-municipality","qatar-monthly-statistics-transactions-through-qatar-e-government","Qatar Monthly Statistics Marriages By Nationality","qatar-monthly-statistics-population-by-age-group",
          "qatar-monthly-statistics-marriages","qatar-monthly-statistics-population-by-gender","qms-deaths-by-nationality",
          "qms-divorces","qms-divorces-by-nationality-gender","qms-live-births","qatar-monthly-statistics-total-population-of-2022","qatar-monthly-statistics-tourism",
          "qatar-monthly-statistics-money-supply","qatar-monthly-statistics-qatar-exchange-number-of-shares"]

   print (f"topic match:= {difflib.get_close_matches(query,lst,n=1,cutoff=0)[0]}")
   return difflib.get_close_matches(query,lst,n=1,cutoff=0)[0]



def call_api(category):
    print(category)
    print(f"{constants.BASE_URL}{category}/records?limit=1")
    response = requests.get(f"{constants.BASE_URL}{category}/records?limit=1")
    print(response.json())
    return response.json() 

# call_api("qatar-monthly-statistics-money-supply")

