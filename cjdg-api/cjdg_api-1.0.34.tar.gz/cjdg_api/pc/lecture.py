from requests.api import delete
from ..base import base
from loguru import logger


class lecture(base):
    url = "https://client.chaojidaogou.com/allstar/api/lecture/"

    def __init__(self, token):
        super().__init__(token)

    def list(self, nowPage=1, pageSize=100, ordertype=3, orderflag=0, status=1, skillids=""):
        url = f"{self.url}getLecturerList"
        params = {
            "nowPage": nowPage,
            "pageSize": pageSize,
            "ordertype": ordertype,
            "orderflag": orderflag,
            "status": status,
            "skillids": skillids,
        }
        resp = self.request(
            url=url,
            params=params,
            method="GET"
        )
        code = resp.get("code")
        if code == 102:
            return resp.get("dataObject").get("list")
        logger.error({
            "msg": "讲师列表请求错误",
            "params": params,
            "response": resp
        })

    def read(self, id):
        pass

    def update(self, data):
        pass

    def delete(self, id):
        pass

    def create(self, userIds, flag=0, tagIds=941, des=""):
        url = f"{self.url}addUserAsLecturer"
        params = {
            "userIds": userIds,
            "flag": flag,
            "tagIds": tagIds,
            "des": des,
        }
        return self.request(
            url=url,
            params=params,
            method="POST"
        )
