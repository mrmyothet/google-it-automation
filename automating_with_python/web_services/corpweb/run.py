#!/usr/bin/env python3

import os
import requests

data_path = "/data/feedback"

for filename in os.listdir(data_path):
    with open(data_path + "/" + filename) as file:
        lines = file.readlines()
        feedback = {
            "title": lines[0].strip(),
            "name": lines[1].strip(),
            "date": lines[2].strip(),
            "feedback": lines[3].strip(),
        }
        response = requests.post("http://35.227.136.102/feedback/", json=feedback)
        if not response.ok:
            raise Exception(
                "POST failed! | Status code: {} | File: {}".format(
                    response.status_code, filename
                )
            )
        print("Feedback uploaded successfully! | File: {}".format(filename))
