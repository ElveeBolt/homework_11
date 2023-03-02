from threading import Thread
from datetime import datetime
from multiprocessing import Process


def runtime_function(func):
    """
    Decorator for get delta time of function work
    :param func: object of func
    :return:
    """

    def wrapper(*args, **kwargs):
        time_start = datetime.now()
        func(*args, **kwargs)
        time_stop = datetime.now()
        print(time_stop - time_start)

    return wrapper


def get_tickets(start: int, stop: int) -> list:
    """
    Get list of tickets by start and stop params
    :param start: int of start
    :param stop: insf of stop
    :return: list of tickets
    """
    return [f'{ticket:06}' for ticket in range(start, stop + 1)]


@runtime_function
def get_lucky(tickets: list):
    """
    Gel all lucky and unlucky number of tickets
    :param tickets: list of tickets
    :return:
    """
    lucky = 0
    unlucky = 0

    for ticket in tickets:
        ticket = [int(i) for i in ticket]
        if sum(ticket[:3]) == sum(ticket[3:]):
            lucky += 1
        else:
            unlucky += 1

    print(f'Lucky ticket - {lucky}')
    print(f'Unlucky ticket - {unlucky}')


def main():
    # One task
    tickets = get_tickets(start=0, stop=999999)
    get_lucky(tickets)

    # Two task Threading
    print('\nTime work with two task - Threading')
    tickets1 = get_tickets(start=0, stop=500000)
    tickets2 = get_tickets(start=500001, stop=999999)
    thread1 = Thread(target=get_lucky, args=(tickets1,))
    thread2 = Thread(target=get_lucky, args=(tickets2,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    # Two task Process
    print('\nTime work with two task - Process')
    tickets1 = get_tickets(start=0, stop=500000)
    tickets2 = get_tickets(start=500001, stop=999999)
    process1 = Process(target=get_lucky, args=(tickets1,))
    process2 = Process(target=get_lucky, args=(tickets2,))
    process1.start()
    process2.start()
    process1.join()
    process2.join()


if __name__ == '__main__':
    main()
