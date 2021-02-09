import os
import subprocess
import time

import requests


class TestInfrastructure:
    INFRA = os.path.dirname(os.path.abspath(__file__))
    TEST_URL = "http://localhost:8080"

    def reset(self):
        print(f"$ docker-compose down -v")
        p = subprocess.Popen(["docker-compose", "down", "-v"], cwd=self.INFRA)
        p.wait()
        print(f"$ docker-compose up -d")
        p = subprocess.Popen(["docker-compose", "up", "-d"], cwd=self.INFRA)
        p.wait()
        response_code = self.__check_response()
        retries = 1
        while response_code != 200:
            print(f"---------------> BRINGING UP (Number of retries: {retries}")
            time.sleep(5)
            response_code = self.__check_response()
            retries += 1
        print("################################################")
        print("################################################")
        print("################# UP & RUNNING #################")
        print("################################################")
        print("################################################")

    def __check_response(self):
        try:
            return requests.get(self.TEST_URL).status_code
        except:
            return 0
