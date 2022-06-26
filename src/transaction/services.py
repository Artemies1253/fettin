from typing import Union

from src.user.models import User
from src.currency.models import Currency, CurrencyUser
from src.transaction.models import TransactionExchange, TransactionReplenishment


def do_subtraction(
        buyer_currency: CurrencyUser, seller_currency: CurrencyUser,
        value_buyer: float, value_seller: float
):
    """Вычитает валюту у продавца и у покупателя"""
    if buyer_currency.count == value_buyer:
        buyer_currency.delete()
    else:
        buyer_currency.count -= value_buyer
        buyer_currency.save()

    if seller_currency.count == value_seller:
        seller_currency.delete()
    else:
        seller_currency.count -= value_buyer
        seller_currency.save()


def make_addition(
        buyer: User, seller: User,
        value_buyer: float, value_seller: float,
        kind_currency_buyer: Currency, kind_currency_seller: Currency):
    """Добавляет валюту продавцу и покупателю"""
    queryset_currency_buyer = CurrencyUser.objects.filter(user=buyer, currency=kind_currency_seller)

    if queryset_currency_buyer.exists():
        currency_buyer = queryset_currency_buyer.first()
        currency_buyer.count += value_seller
        currency_buyer.save()
    else:
        CurrencyUser.objects.create(user=buyer, currency=kind_currency_seller, count=value_seller)

    currency_seller = CurrencyUser.objects.filter(user=seller, currency=kind_currency_buyer)

    if currency_seller.exists():
        currency_seller = currency_seller.first()
        currency_seller.count += value_buyer
        currency_seller.save()
    else:
        CurrencyUser.objects.create(user=seller, currency=kind_currency_buyer, count=value_buyer)


def change_currency_value(
        buyer: User, seller: User,
        value_buyer: float, value_seller: float,
        kind_currency_buyer: Currency, kind_currency_seller: Currency
) -> bool:
    """Изменяет валютный баланс пользователей"""
    buyer_currency = CurrencyUser.objects.get(user=buyer, currency=kind_currency_buyer)
    seller_currency = CurrencyUser.objects.get(user=seller, currency=kind_currency_seller)
    do_subtraction(
        buyer_currency=buyer_currency, seller_currency=seller_currency,
        value_buyer=value_buyer, value_seller=value_seller
    )
    make_addition(
        buyer=buyer, seller=seller,
        value_buyer=value_buyer, value_seller=value_seller,
        kind_currency_buyer=kind_currency_buyer, kind_currency_seller=kind_currency_seller
    )


def create_exchange_transaction(
        buyer: User, seller: User,
        value_buyer: float, value_seller: float,
        kind_currency_buyer: Currency,
        kind_currency_seller: Currency
) -> Union[TransactionExchange, bool]:
    """
    Создаёт транзакцию между 2 пользователями
    :param buyer: Продавец
    :param seller: Покупатель
    :param value_buyer: Количество валюты которое тратит покупатель
    :param value_seller: Количество валюты которое тратит продавец
    :param kind_currency_buyer: Вид валюты которую тратит покупатель
    :param kind_currency_seller: Вид валюты которую тратит продавец
    :return: Созданная транзакция
    """
    if change_currency_value(buyer, seller, value_buyer, value_seller, kind_currency_buyer, kind_currency_seller):

        return TransactionExchange.objects.create(
            buyer=buyer, seller=seller, value_buyer=value_buyer, value_seller=value_seller,
            currency_buyer=kind_currency_buyer, currency_seller=kind_currency_seller)
    else:
        return False


def change_user_balance(user: User, currency: Currency, count: float):
    currency_user = CurrencyUser.objects.filter(user=user, currency=currency)
    if currency_user.exists():
        currency_user = currency_user.first()
        currency_user.count += count
        currency_user.save()
    else:
        CurrencyUser.objects.create(user=user, currency=currency, count=count)


def create_replenishment_transaction(user: User, currency: Currency, count: float):
    change_user_balance(user=user, currency=currency, count=count)
    return TransactionReplenishment.objects.create(user=user, value=count, currency=currency)
