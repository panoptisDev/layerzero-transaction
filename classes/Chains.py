from utils.config import MERKLY_CONTRACTS, CHAIN_IDS


class Networks:
    chain: str
    contract_address: str

    class Arbitrum:
        chain = 'arbitrum'
        contract_address = MERKLY_CONTRACTS[chain]

    class ArbitrumNova:
        chain = 'arbitrum-nova'
        contract_address = MERKLY_CONTRACTS[chain]

    class Optimism:
        chain = 'optimism'
        contract_address = MERKLY_CONTRACTS[chain]

    class ZkSync:
        chain = 'zksync'
        contract_address = MERKLY_CONTRACTS[chain]

    class PolygonZKevm:
        chain = 'polygon-zkevm'
        contract_address = MERKLY_CONTRACTS[chain]


class DestinationChains:
    chain: str
    chainId: int

    class Arbitrum:
        chain = Networks.Arbitrum.chain
        chainId = CHAIN_IDS[chain]

    class ArbitrumNova:
        chain = Networks.ArbitrumNova.chain
        chainId = CHAIN_IDS[chain]

    class Optimism:
        chain = Networks.Optimism.chain
        chainId = CHAIN_IDS[chain]

    class ZkSync:
        chain = Networks.ZkSync.chain
        chainId = CHAIN_IDS[chain]

    class PolygonZKevm:
        chain = Networks.PolygonZKevm.chain
        chainId = CHAIN_IDS[chain]

    class Zora:
        chain = 'zora'
        chainId = CHAIN_IDS[chain]

    class Scroll:
        chain = 'scroll'
        chainId = CHAIN_IDS[chain]

    class Polygon:
        chain = 'polygon'
        chainId = CHAIN_IDS[chain]

    class Moonbeam:
        chain = 'moonbeam'
        chainId = CHAIN_IDS[chain]

    class Moonriver:
        chain = 'moonriver'
        chainId = CHAIN_IDS[chain]

    class Canto:
        chain = 'canto'
        chainId = CHAIN_IDS[chain]

    class Harmony:
        chain = 'harmony'
        chainId = CHAIN_IDS[chain]
