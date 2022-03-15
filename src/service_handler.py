import json
from typing import Dict
from enum import Enum
import requests
from src.config_manager import ConfigManager
from src.database_commander import DB_COMMANDER
from src.logger_handler import LoggerHandler


class Posttype(Enum):
    TEAMDATA = "teamdata"
    COCKTAIL = "cocktail"
    FILE = "file"


class ServiceHandler(ConfigManager):
    """Class to handle all calls to the mircoservice within the docker"""

    def __init__(self):
        super().__init__()
        self.base_url = self.MICROSERVICE_BASE_URL
        self.logger = LoggerHandler("microservice", "service_logs")
        self.headers = {"content-type": "application/json"}

    def post_cocktail_to_hook(self, cocktailname: str, cocktail_volume: int) -> Dict:
        """Post the given cocktail data to the microservice handling internet traffic to send to defined webhook"""
        if not self.MICROSERVICE_ACTIVE:
            return service_disabled()
        # calculate volume in litre
        data = {
            "cocktailname": cocktailname,
            "volume": cocktail_volume,
            "machinename": self.MAKER_NAME,
            "countrycode": self.UI_LANGUAGE,
        }
        payload = json.dumps(data)
        endpoint = f"{self.base_url}/hookhandler/cocktail"
        return self.__try_to_send(endpoint, Posttype.COCKTAIL, payload=payload)

    def send_mail(self, file_name: str, binary_file) -> Dict:
        """Post the given file to the microservice handling internet traffic to send as mail"""
        if not self.MICROSERVICE_ACTIVE:
            return service_disabled()
        endpoint = f"{self.base_url}/email"
        files = {"upload_file": (file_name, binary_file,)}
        return self.__try_to_send(endpoint, Posttype.FILE, files=files)

    def post_team_data(self, team_name: str, cocktail_volume: int) -> Dict:
        """Post the given team name to the team api if activated"""
        if not self.TEAMS_ACTIVE:
            return team_disabled()
        payload = json.dumps({"team": team_name, "volume": cocktail_volume})
        endpoint = f"{self.TEAM_API_URL}/cocktail"
        return self.__try_to_send(endpoint, Posttype.TEAMDATA, payload=payload)

    def __try_to_send(self, endpoint: str, post_type: Posttype, payload: str = None, files: dict = None) -> Dict:
        """Try to send the data to the given endpoint.
        Logs the action, catches and logs if there is no connection.
        Raises an exception if there is no data to send.

        Args:
            endpoint (str): url to send
            post_type (Posttype): Addional info for logger what was posted.
            payload (str, optional): JSON data for payload. Defaults to None.
            files (dict, optional): dict with key 'upload_file' + filename and binary data as tuple. Defaults to None.

        Raises:
            Exception: There is no data to send. This shouldn't be happening if used correctly.

        Returns:
            Dict: Statuscode and message, or empty if cannot reach service
        """
        try:
            if payload is not None:
                req = requests.post(endpoint, data=payload, headers=self.headers, timeout=3)
                # if successfully send to teams, see if there are other to send.
                if post_type is Posttype.TEAMDATA:
                    self.__check_failed_data()
            elif files is not None:
                req = requests.post(endpoint, files=files, timeout=3)
            else:
                raise ValueError('Neither payload nor files given!')
            message = str(req.text).replace("\n", "")
            self.logger.log_event("INFO", f"Posted {post_type.value} to {endpoint} | {req.status_code}: {message}")
            return {
                "status": req.status_code,
                "message": message,
            }
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            self.__log_connection_error(endpoint, post_type)
            # only save failed team data for now
            if post_type is Posttype.TEAMDATA:
                DB_COMMANDER.save_failed_teamdata(payload)
            return {}

    def __log_connection_error(self, endpoint: str, post_type: Posttype):
        self.logger.log_event("ERROR", f"Could not connect to: '{endpoint}' for {post_type.value}")

    def __check_failed_data(self):
        """Gets one failed teamdata and sends it"""
        endpoint = f"{self.TEAM_API_URL}/cocktail"
        failed_data = DB_COMMANDER.get_failed_teamdata()
        if failed_data:
            msg_id, payload = failed_data
            # Delete the old thing before recursion hell comes live
            DB_COMMANDER.delete_failed_teamdata(msg_id)
            self.__try_to_send(endpoint, Posttype.TEAMDATA, payload)


def service_disabled():
    """Return that microservice is disabled"""
    return {
        "status": 503,
        "message": "Microservice disabled",
    }


def team_disabled():
    """Return that teams is disabled"""
    return {
        "status": 503,
        "message": "Teams disabled",
    }


SERVICE_HANDLER = ServiceHandler()
