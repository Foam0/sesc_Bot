from collections import defaultdict

import requests


def get(date, group):
    # if date == 0 or date == 7:
    #    return dict({"subject": "Воскреснье", "teacher": "", "auditory": ""})
    x = (requests.get(f"https://lyceum.urfu.ru/?type=11&scheduleType=group&weekday={str(date)}&group={str(group)}"))
    x = x.json()
    a = x["lessons"] + x["diffs"]
    s = defaultdict(lambda: defaultdict(dict))
    for i in a:
        if i["subgroup"] == 0:
            s[i["number"]][1] = {"subject": i["subject"], "teacher": i["teacher"], "auditory": i["auditory"]}
            s[i["number"]][2] = {"subject": i["subject"], "teacher": i["teacher"], "auditory": i["auditory"]}
        else:
            s[i["number"]][i["subgroup"]] = {"subject": i["subject"], "teacher": i["teacher"],
                                             "auditory": i["auditory"]}
    for i in range(min(s.keys()), max(s.keys()) + 1):
        if 1 not in s[i].keys():
            s[i][1] = {"subject": "relax ||", "teacher": "",
                       "auditory": ""}
        if 2 not in s[i].keys():
            s[i][2] = {"subject": "|| relax", "teacher": "",
                       "auditory": ""}
    return s
