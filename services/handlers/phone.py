from typing import Optional

from services.decorators import input_error, route
from services.utils import AddressBook


@route('add-phone')
@input_error
def add_phone_to_contact(name: str) -> str:
    """
    По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта.
    Пользователь вводит команду add-phone и имя, обязательно через пробел.
    Пример команды: add-phone UserName
    """
    contact = AddressBook()[name]

    phone = contact.add_phone(input("Enter phone number: "))

    return f"Contact phone number {name} '{phone.value}' successfully added"


@route("change-phone")
@input_error
def change_contact_phone(name: str) -> Optional[str]:
    """
    По этой команде бот заменяет старый номер телефона новым для существующего контакта.
    Пользователь вводит команду change-phone и имя, обязательно через пробел.
    Далее пользователю будет предложено выбрать из списка номер, который необходимо заменить новым.
    Пример команды: change-phone UserName 
    """
    contact = AddressBook()[name]

    new_phone = input("Enter a new phone number: ")

    while True:
        print(contact_phones(name))

        try:
            index = int(
                input("Enter the index number of the phone from the list you want to replace: "))
        except ValueError:
            print("\nChoose a number from the list!")
            print("\n(Enter 0 to cancel)")
            continue

        if index == 0:
            return

        try:
            new_phone = contact.replace_phone(index, new_phone)
        except IndexError:
            print("\nChoose a number from the list!")
            print("\n(Enter 0 to cancel)")
        else:
            break

    return f"Contact {name} phone number has been successfully replaced to '{new_phone.value}'"


@route("remove-phone")
@input_error
def remove_contact_phone(name: str) -> Optional[str]:
    """
    По этой команде бот удаляет номер телефона существующего контакта.
    Пользователь вводит команду remove-phone и имя, обязательно через пробел.
    Далее будет предложено выбрать номер из списка, который необходимо удалить.
    Пример команды: remove-phone UserName
    """
    contact = AddressBook()[name]

    while True:
        print(contact_phones(name))

        try:
            index = int(
                input("Enter the index number of the phone from the list you want to remove: "))
        except ValueError:
            print("\nChoose a number from the list!")
            print("\n(Enter 0 to cancel)")
            continue

        if index == 0:
            return

        try:
            phone = contact.remove_phone(index)
        except IndexError:
            print("\nChoose a number from the list!")
            print("\n(Enter 0 to cancel)")
        else:
            break

    return f"\nContact phone number {name} '{phone.value}' deleted successfully"


@route("phone")
@input_error
def contact_phones(name: str) -> str:
    """
    По этой команде бот выводит в консоль номера телефонов для указанного контакта.
    Пользователь вводит команду phone и имя контакта, чьи номера нужно показать, обязательно через пробел.
    Пример команды: phone UserName
    """
    contact = AddressBook()[name]

    return (f"Phone numbers of {name}\n\t" +
            "\n\t".join([f"{num}. {x.value}" for num, x in enumerate(contact.phones, 1)]))
