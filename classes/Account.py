import asyncio
import random

from eth_account import Account as EthereumAccount
from loguru import logger
from web3 import AsyncWeb3
from web3.middleware import async_geth_poa_middleware
from web3.types import TxParams

from utils.config import ERC20_ABI, RPC


class Account:
    def __init__(self, account_id: int, private_key: str, chain: str, proxy: str | None) -> None:
        self.account_id = account_id
        self.private_key = private_key
        self.chain = chain
        self.explorer = RPC[chain]['explorer']
        self.token = RPC[chain]['token']
        
        request_kwargs = {}
        if proxy:
            request_kwargs = {'proxy': f'http://{proxy}'}
            
        self.w3 = AsyncWeb3(
            AsyncWeb3.AsyncHTTPProvider(random.choice(RPC[chain]['rpc'])),
            middlewares=[async_geth_poa_middleware],
            request_kwargs=request_kwargs
        )

        self.account = EthereumAccount.from_key(private_key)
        self.address = self.account.address
    
    async def get_amount(
        self,
        min_amount: float,
        max_amount: float,
        decimal: int,
        all_amount: bool,
        min_percent: int,
        max_percent: int
    ) -> [int, float, float]:
        random_amount = round(random.uniform(min_amount, max_amount), decimal)
        random_percent = random.randint(min_percent, max_percent)
        
        percent = 1 if random_percent == 100 else random_percent / 100
        
        balance = await self.w3.eth.get_balance(self.address)
        amount_wei = int(balance * percent) if all_amount else self.w3.to_wei(random_amount, 'ether')
        amount = self.w3.from_wei(int(balance * percent), 'ether') if all_amount else random_amount
        
        return amount_wei, amount, balance
    
    def get_contract(self, contract_address: str, abi = None):
        contract_address = self.w3.to_checksum_address(contract_address)
        
        if abi is None:
            abi = ERC20_ABI
        
        contract = self.w3.eth.contract(address=contract_address, abi=abi)
        
        return contract
    
    async def get_tx_data(self, value: int = 0) -> dict:
        tx = {
            'chainId': await self.w3.eth.chain_id,
            'from': self.address,
            'value': value,
            'gasPrice': await self.w3.eth.gas_price,
            'nonce': await self.w3.eth.get_transaction_count(self.address)
        }
        return tx
    
    async def execute_transaction(self, contract_txn: TxParams):
        signed_txn = await self.sign(contract_txn)
        txn_hash = await self.send_raw_transaction(signed_txn)
        return txn_hash
    
    async def sign(self, transaction):
        gas = await self.w3.eth.estimate_gas(transaction)
        
        transaction.update({'gas': gas})
        
        signed_tx = self.w3.eth.account.sign_transaction(transaction, self.private_key)
        return signed_tx
    
    async def send_raw_transaction(self, signed_txn):
        txn_hash = await self.w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        return txn_hash
    
    async def wait_until_tx_finished(self, hash: str):
        while True:
            receipts = await self.w3.eth.get_transaction_receipt(hash)
            status = receipts.get('status')

            if status == 1:
                return logger.success(f'{self.account_id} | {self.address} | {self.explorer}{hash.hex()} successfully!')
            elif status is None:
                await asyncio.sleep(1)
            else:
                return logger.success(f'{self.account_id} | {self.address} | {self.explorer}{hash.hex()} transaction failed!')