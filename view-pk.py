import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exchange.settings')
from django.conf import settings
import django
django.setup()

from lib.cipher import AESCoderDecoder
from cryptocoins.models.keeper import GasKeeper
from core.models.cryptocoins import UserWallet

def main():
    user_deposit_wallet_private_keys_dict = dict(UserWallet.objects.filter(
        currency='USDT'
    ).values_list(
        'address',
        'private_key'
    ))

    gas_keeper_dict = dict(GasKeeper.objects.filter().values_list(
        'user_wallet__address',
        'user_wallet__private_key',
    ))

    print("User deposit address private key")
    for address, private_key in user_deposit_wallet_private_keys_dict.items():
        print(address)
        print(AESCoderDecoder(settings.CRYPTO_KEY).decrypt(private_key))
        print("==========")

    print("Gas keeper address & private key")
    for user_wallet__address, user_wallet__private_key in gas_keeper_dict.items():
        print(user_wallet__address)
        print(AESCoderDecoder(settings.CRYPTO_KEY).decrypt(user_wallet__private_key))
        print("==========")

    return

if __name__ == '__main__':
    print('Start')
    main()
    print('Stop')