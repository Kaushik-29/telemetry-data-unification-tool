from types import resolve_bases
import json, unittest

from datetime import datetime

with open("./data-1.json", "r") as f:
    jsonData1 = json.load(f)
with open("./data-2.json", "r") as f:
    jsonData2 = json.load(f)
with open("./data-result.json", "r") as f:
    jsonExpectedResult = json.load(f)


def isotomin(iso):
    iso = iso.replace("Z", "+00:00")
    return int(datetime.fromisoformat(iso).timestamp() * 1000)


def convertFromFormat1(jsonObject):

    # IMPLEMENT: Conversion From Type 1
    # now we are creating a directory called "result"

    result = {}
    result["deviceID"] = jsonObject["deviceID"]
    result["deviceType"] = jsonObject["deviceType"]
    result["timestamp"] = jsonObject["timestamp"]

    parts = jsonObject["location"].split("/")
    result["location"] = {
        "country": parts[0],
        "city": parts[1],
        "area": parts[2],
        "factory": parts[3],
        "section": parts[4]
    }

    result["data"] = {
        "status": jsonObject["operationStatus"],
        "temperature": jsonObject["temp"]
    }

    return result


def convertFromFormat2(jsonObject):

    # IMPLEMENT: Conversion From Type 1
    # now we are creating a directory called "result"

    result = {}

    result["deviceID"] = jsonObject.get("device").get("id")
    result["deviceType"] = jsonObject.get("device").get("type")
    result["timestamp"] = isotomin(jsonObject["timestamp"])
    result["location"] = {
        "country": jsonObject["country"],
        "city": jsonObject["city"],
        "area": jsonObject["area"],
        "factory": jsonObject["factory"],
        "section": jsonObject["section"]
    }
    result["data"] = jsonObject["data"]
    return result


def main(jsonObject):

    result = {}

    if (jsonObject.get('device') == None):
        result = convertFromFormat1(jsonObject)
    else:
        result = convertFromFormat2(jsonObject)

    return result


class TestSolution(unittest.TestCase):

    def test_sanity(self):

        result = json.loads(json.dumps(jsonExpectedResult))
        self.assertEqual(result, jsonExpectedResult)

    def test_dataType1(self):

        result = main(jsonData1)
        self.assertEqual(result, jsonExpectedResult,
                         'Converting from Type 1 failed')

    def test_dataType2(self):

        result = main(jsonData2)
        self.assertEqual(result, jsonExpectedResult,
                         'Converting from Type 2 failed')


if __name__ == '__main__':
    unittest.main()
