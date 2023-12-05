import random

from modules.merkly import Merkly
from classes.Chains import DestinationChains
import route_settings as rs

async def random_route(account_id: int, key: str, proxy: str):
    routes = {
        'Arbitrum': bridge_arbitrum,
        'ArbitrumNova': bridge_arbitrum_nova,
        'Optimism': bridge_optimism,
        'ZkSync': bridge_zksync,
        'PolygonZkEvm': bridge_polygon_zkevm,
        'Zora': bridge_zora,
        'Scroll': bridge_scroll,
        'Polygon': bridge_polygon,
        'Moonbeam': bridge_moonbeam,
        'Moonriver': bridge_moonriver,
        'Canto': bridge_canto,
        'Harmony': bridge_harmony
    }
    
    random_routes = [route for name, route in routes.items() if getattr(rs, name).use_in_random_routes]

    choice = random.choice(random_routes)
    await choice(account_id, key, proxy)
    
async def bridge_route(route, account_id: int, key: str, proxy: str):
    min_amount = getattr(rs, route).min_amount
    max_amount = getattr(rs, route).max_amount
    decimal = getattr(rs, route).decimal
    
    merkly_refuel = Merkly(account_id, key, proxy, getattr(DestinationChains, route))
    await merkly_refuel.merkly_refuel(min_amount, max_amount, decimal)

async def bridge_arbitrum(account_id: int, key: str, proxy: str):
    await bridge_route('Arbitrum', account_id, key, proxy)

async def bridge_arbitrum_nova(account_id: int, key: str, proxy: str):
    await bridge_route('ArbitrumNova', account_id, key, proxy)

async def bridge_optimism(account_id: int, key: str, proxy: str):
    await bridge_route('Optimism', account_id, key, proxy)
    
async def bridge_zksync(account_id: int, key: str, proxy: str):
    await bridge_route('ZkSync', account_id, key, proxy)

async def bridge_polygon_zkevm(account_id: int, key: str, proxy: str):
    await bridge_route('PolygonZkEvm', account_id, key, proxy)

async def bridge_zora(account_id: int, key: str, proxy: str):
    await bridge_route('Zora', account_id, key, proxy)

async def bridge_scroll(account_id: int, key: str, proxy: str):
    await bridge_route('Scroll', account_id, key, proxy)

async def bridge_polygon(account_id: int, key: str, proxy: str):
    await bridge_route('Polygon', account_id, key, proxy)

async def bridge_moonbeam(account_id: int, key: str, proxy: str):
    await bridge_route('Moonbeam', account_id, key, proxy)

async def bridge_moonriver(account_id: int, key: str, proxy: str):
    await bridge_route('Moonriver', account_id, key, proxy)

async def bridge_canto(account_id: int, key: str, proxy: str):
    await bridge_route('Canto', account_id, key, proxy)

async def bridge_harmony(account_id: int, key: str, proxy: str):
    await bridge_route('Harmony', account_id, key, proxy)