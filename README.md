![LayerZero](https://i.imgur.com/rX6SXJ0.png)

---

With this repository you will be able to send transactions to **Merkly** interacting with the **LayerZero** protocol.

Transactions are created through the gas delivery function in blockchains that support the **LayerZero** protocol.

Transactions are only sent from **Arbitrum, Arbitrum-Nova, Optimism, ZkSync, PolygonZKEvm** to some of the cheapest blockchains such as: **Arbitrum Nova, Zora, Scroll, Polygon, Moonbeam, Moonriver, Canto, Harmony** and others.

You can also enable random choice routes to do random activity on LayerZero for your accounts.

## INSTALLATION

1. Install **Python 3.11+**.
2. `git clone https://github.com/holmenov/LayerZero-Transactions.git`.
3. `cd LayerZero-Transactions`.
4. `pip install -r requirements.txt`.
5. Paste your proxies into `proxy.txt` in `ip:port@login:password` format
6. Paste the wallet private key in `accounts.txt`.
7. Set the general settings in `settings.py`.
8. Set the routes settings in `route_settings.py`.

## GENERAL SETTINGS

- `MAX_GAS` - Maximum GAS in GWEI for transactions [Integer].
- `RANDOM_WALLET` - Random wallet mode [Boolean].
- `REMOVE_WALLET` - Remove wallet after work [Boolean].
- `USE_PROXY` - Proxy mode [Boolean].
- `MAX_WORKERS` - Quantity threads [Integer].
- `WORKER_SLEEP_FROM`, `WORKER_SLEEP_TO` - Interval in seconds between thread starts [Integer].
- `SLEEP_AFTER_WORK_FROM`, `SLEEP_AFTER_WORK_TO` - Seconds to sleep after completing a task [Integer].
- `SEND_FROM` - Blockchain sender [Class].

## ROUTES SETTINGS

You can set different settings for each route.

- `min_amout` - Minimum amount in ETH
- `max_amout` - Maximum amount in ETH
- `decimal` - Number of decimal places to generate a random number in ETH
- `use_in_random_routes` - Do you want to use this route in random routes