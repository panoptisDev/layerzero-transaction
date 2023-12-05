from loguru import logger
import questionary

from classes.Threads import Threads
from utils.routes import *
from utils.utils import get_wallets


def get_module():
    routes = [
        questionary.Choice('1) Random routes', random_route),
        questionary.Choice('2) Merkly | Arbitrum Nova', bridge_arbitrum_nova), # 0.28$ - 40 GWEI
        questionary.Choice('3) Merkly | Zora', bridge_zora), # 0.18$ - 40 GWEI
        questionary.Choice('4) Merkly | Scroll', bridge_scroll), # 0.4$ - 40 GWEI
        questionary.Choice('5) Merkly | Polygon', bridge_polygon), # 0.38$ - 40 GWEI
        questionary.Choice('6) Merkly | Moonbeam', bridge_moonbeam), # 0.06$ - 40 GWEI
        questionary.Choice('7) Merkly | Moonriver', bridge_moonriver), # 0.06$ - 40 GWEI
        questionary.Choice('8) Merkly | Canto', bridge_canto), # 0.2$ - 40 GWEI
        questionary.Choice('9) Merkly | Harmony', bridge_harmony), # 0.05$ - 40 GWEI
    ]

    route = questionary.select(
        'Choose your route:',
        choices=routes,
        qmark='📌 ',
        pointer='➡️ '
    ).ask()

    return route

def main():
    module = get_module()
    data = get_wallets()
    
    threads = Threads(data)
    threads.start_workers(module=module)

if __name__ == '__main__':
    logger.add('logs.log')
    main()