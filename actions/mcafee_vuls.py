import requests
import xmltodict
import datetime
import re
import pandas as pd
import os
from st2common.runners.base_action import Action

class McAfee_New_Vuls(Action):

    def run(self, days):
        try:
            trigger = False  # Trigger for any new found items
            file = os.getcwd() + "\\threats.csv"  # Creates a file for the Users PC
            link = "https://www.mcafee.com/enterprise/resources/security-bulletins/security-bulletins.xml"  # Location to grab XML
            # Time limit, exe should be run every 24 hours
            print(days)
            print(type(days))
            if (days != -999):
                print("Test run with " + str(days) + " Days")
                compare_time = datetime.datetime.now() - datetime.timedelta(days=days, hours=2)
            else:
                print("Days run with Default")
                compare_time = datetime.datetime.now() - datetime.timedelta(days=1, hours=2)
            # ---------------- Getting to the required data
            response = requests.get(link)
            x = response.content
            x = xmltodict.parse(x)
            x = x["autnresponse"]
            x = x["responsedata"]
            y = x['autn:hit']
            # ---------------- End of getting to required data
            items = {}  # Empty list to store values
            latest_items = []
            for i in range(0, len(y)):
                published = int(y[i]["autn:content"]["DOCUMENT"]["CREATE_DATE"])
                last_modified = int(y[i]["autn:content"]["DOCUMENT"]["LAST_MODIFIED"])
                if latest_items > published:
                    published = last_modified
                published = datetime.datetime.fromtimestamp(published / 1000).strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]
                published_datetime = datetime.datetime.strptime(published, '%Y-%m-%d')
                if published_datetime < compare_time:
                    break
                lick = y[i]["autn:reference"].split("_")[0]
                title = re.split(r'[-(]', y[i]["autn:title"])[1]
                lick = "https://kc.mcafee.com/corporate/index?page=content&id=" + lick
                item = {}
                item["title"] = title
                item["date"] = published
                item["link"] =lick
                print(item)
                items[i] = item  # Appending any found items to the overall list

            return True, items
        except Exception as e:
            return False, {'error':e}

