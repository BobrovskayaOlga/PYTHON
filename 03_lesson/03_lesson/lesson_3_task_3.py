from address import Address
from mailing import Mailing

to_addr = Address('309501', 'Старый Оскол', 'ул.Хмелева', '10', '5')
from_addr = Address('654321', 'Санкт-Петербург', 'Невская ул.', '20', '10')

mailing = Mailing(to_addr, from_addr, 500, 'TRACK123456')

output_message = (
    f'Отправление {mailing.track} '
    f'из {mailing.from_address.index}, {mailing.from_address.city}, '
    f'{mailing.from_address.street}, {mailing.from_address.house}-'
    f'{mailing.from_address.apartment} '
    f'в {mailing.to_address.index}, {mailing.to_address.city}, '
    f'{mailing.to_address.street}, {mailing.to_address.house}-'
    f'{mailing.to_address.apartment}. '
    f'Стоимость {mailing.cost} рублей.'
)

print(output_message)
