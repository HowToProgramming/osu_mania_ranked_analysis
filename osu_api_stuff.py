from requests import get
from datetime import date
from osuapitoken import token


def get_approved_beatmap_since(d: date):
    url = f"https://osu.ppy.sh/api/get_beatmaps?k={token}&m=3&since={d.year}-{d.month}-{d.day}"
    return get(url).json()

def get_ranked_beatmap_at(d: date):
    data = get_approved_beatmap_since(d)
    status_ranked = "1"
    ranked_at = d.strftime("YYYY-MM-DD")
    return list(filter(lambda beatmap: beatmap['approved'] == status_ranked and ranked_at in beatmap['approved_date'], data))
