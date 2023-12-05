from loguru import logger
from eth_abi import encode

from classes.Account import Account
from utils.config import MERKLY_ABI
from settings import SEND_FROM
from classes.Chains import DestinationChains
from utils.wrappers import check_gas


class Merkly(Account):
    def __init__(self, account_id: int, private_key: str, proxy: str | None, destination_chain: DestinationChains) -> None:
        super().__init__(account_id=account_id, private_key=private_key, proxy=proxy, chain=SEND_FROM.chain)
        
        self.destination_chain = destination_chain
        self.merkly_contract = self.get_contract(SEND_FROM.contract_address, MERKLY_ABI)
    
    def get_adapterParams(self, gasLimit: int, amount_wei: int) -> str:
        _adapterParams = self.w3.to_hex(encode(["uint16", "uint64", "uint256"], [2, gasLimit, amount_wei])[30:])
        _adapterParams = _adapterParams + self.address[2:]
        return _adapterParams
    
    async def get_gas_bridge_fee(self, amount_wei: int) -> int:
        adapterParams = self.get_adapterParams(250000, amount_wei)
        
        estimateGasBridgeFee = await self.merkly_contract.functions.estimateGasBridgeFee(
            self.destination_chain.chainId, False, adapterParams
        ).call()
        estimateGasBridgeFee = estimateGasBridgeFee[0]
    
        return estimateGasBridgeFee
    
    @check_gas
    async def merkly_refuel(self, min_amount: float, max_amount: float, decimal: int) -> bool:
        if SEND_FROM.chain == self.destination_chain.chain:
            return logger.error(f'{self.account_id} | {self.address} | Bridge to the same network is forbidden.')
        
        logger.info(f'{self.account_id} | {self.address} | Bridge in {self.destination_chain.chain}.')
        
        amount_wei, amount, balance = await self.get_amount(min_amount, max_amount, decimal, False, 1, decimal)
        
        estimateGasBridgeFee = await self.get_gas_bridge_fee(amount_wei)
        
        tx_data = await self.get_tx_data(value=amount_wei)
        tx_data.update({'value': estimateGasBridgeFee})
        
        _adapterParams = self.get_adapterParams(250000, amount_wei)
        
        contract_txn = await self.merkly_contract.functions.bridgeGas(
            self.destination_chain.chainId,
            self.address,
            _adapterParams
        ).build_transaction(tx_data)
        
        txn_hash = await self.execute_transaction(contract_txn)

        await self.wait_until_tx_finished(txn_hash)