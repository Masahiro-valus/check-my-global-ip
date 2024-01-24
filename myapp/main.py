import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_global_ip():
    try:
        response = requests.get('https://ipinfo.io')
        if response.status_code == 200:
            ip_info = response.json()
            global_ip = ip_info.get('ip')
            return global_ip
        else:
            logger.warning(f"IP情報の取得に失敗しました。ステータスコード: {response.status_code}")
            return None
    except requests.RequestException as e:
        logger.error(f"リクエストエラー: {e}")
        return None


def make_request_and_log():
    global_ip = get_global_ip()

    if global_ip:
        logger.info(f"グローバルIPアドレス: {global_ip}")
        url = 'https://google.com'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                logger.info(f"リクエストに成功: {url}")
            else:
                logger.warning(f"リクエストは失敗しました。ステータスコード: {response.status_code}")
        except requests.RequestException as e:
            logger.error(f"リクエストエラー: {e}")


if __name__ == "__main__":
    make_request_and_log()
