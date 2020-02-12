import requests
import xmltodict
import datetime
import re
import pandas as pd
import os

class McAfee_Vuls_Lib():
    # def __init__(self):


    def security_bulletins(self=None):
        link = "https://www.mcafee.com/enterprise/resources/security-bulletins/security-bulletins.xml"  # Location to grab XML
        response = requests.get(link)
        print(response)
        if response.status_code == 200:
            print("Bulletins retrieved correctly")
            return response.content
        else:
            print("Failed to retrieve")
            return response.status_code


    def x_days(self, days):
        if (days != -999):
            print("Test run with " + str(days) + " Days")
            compare_time = datetime.datetime.now() - datetime.timedelta(days=days, hours=2)
        else:
            print("Days run with Default")
            compare_time = datetime.datetime.now() - datetime.timedelta(days=1, hours=2)
        return compare_time

    def harvest_xml(self, xml):
        xml = xmltodict.parse(xml)
        xml = xml["autnresponse"]["responsedata"]['autn:hit']
        return xml

    def affected_list(self, xml, time):
        items = {}  # Empty list to store values
        # latest_items = []
        count = 0
        for i in range(0, len(xml)):
            published = int(xml[i]["autn:content"]["DOCUMENT"]["CREATE_DATE"])
            last_modified = int(xml[i]["autn:content"]["DOCUMENT"]["LAST_MODIFIED"])
            if last_modified > published:
                published = last_modified
            published = datetime.datetime.fromtimestamp(published / 1000).strftime('%Y-%m-%d %H:%M:%S').split(" ")[0]
            published_datetime = datetime.datetime.strptime(published, '%Y-%m-%d')
            if published_datetime < time:
                break
            link = xml[i]["autn:reference"].split("_")[0]
            title = re.split(r'[-(]', xml[i]["autn:title"])[1]
            link = "https://kc.mcafee.com/corporate/index?page=content&id=" + link
            # item = {}
            items.update({"item " + str(count): {"title": title, "date": published, "link": link}})
            count += 1
        return items


    def run(self, days):
        try:
            xml_extract = self.security_bulletins()
        except Exception as e:
            print("Error is :", e)
            return e
        try:
            search_days = self.x_days(days)
        except Exception as e:
            print("Error is :", e)
            return e
        try:
            xml_extract = self.harvest_xml(xml_extract)
        except Exception as e:
            print("Error is :", e)
            return e
        try:
            items = self.affected_list(xml_extract, search_days)
        except Exception as e:
            print("Error is :", e)
            return e
        try:
            return True, items
        except Exception as e:
            return False, {'error':e}







