
import json
import pathlib
import pandas as pd
import pymongo


import requests


API_KEYS = ""


def _get_movie_data_from_imdb_ids():
    try:
        with open("movieid.txt", "r") as fr:
            # mongo_client = pymongo.MongoClient("mongodb://0.0.0.0:27017/")
            # mydb = mongo_client["movie"]
            # mycol = mydb["movie"]
            fw = open("movies.txt", "w")
            for mid in fr.readlines():
                movie_id_ = mid.rstrip()
                movie_url = "https://api.themoviedb.org/3/movie/{}?api_key={}".format(movie_id_, API_KEYS)
                print(movie_url)
                m_res = requests.get(movie_url, verify=False)
                print(m_res.status_code)
                if m_res.status_code == 200:
                    mdata = json.loads(m_res.content)
                    if "success" in mdata.keys():
                        print("Movie data is not found for this id: {}".format(mid))
                    else:
                        print(mdata)
                        fw.write(str(mdata) + '\n')
    except Exception as e:
        print("Error: {}".format(e))



_get_movie_data_from_imdb_ids()
