import os
import time
from typing import Dict

from tabulate import tabulate

from .core import cl, logger, THREADS_PER_CORE, Params, Stats
from .mhddos import Tools


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def show_statistic(
    statistics: Dict[Params, Stats],
    table,
    use_my_ip,
    proxies_cnt,
    time_left
):
    tabulate_text = []
    total_pps, total_bps = 0, 0
    for params, stats in statistics.items():
        pps, bps = stats.reset()
        total_pps += pps
        total_bps += bps
        if table:
            tabulate_text.append((
                f'{cl.YELLOW}%s' % params.target.url.host, params.target.url.port, params.method,
                Tools.humanformat(pps) + "/s", f'{Tools.humanbits(bps)}/s{cl.RESET}'
            ))
        else:
            logger.info(
                f'{cl.YELLOW}Ціль:{cl.BLUE} %s,{cl.YELLOW} Порт:{cl.BLUE} %s,{cl.YELLOW} Метод:{cl.BLUE} %s,'
                f'{cl.YELLOW} Запити:{cl.BLUE} %s/s,{cl.YELLOW} Трафік:{cl.BLUE} %s/s{cl.RESET}' %
                (
                    params.target.url.host,
                    params.target.url.port,
                    params.method,
                    Tools.humanformat(pps),
                    Tools.humanbits(bps),
                )
            )

    if table:
        tabulate_text.append((f'{cl.GREEN}Усього', '', '', Tools.humanformat(total_pps) + "/s",
                              f'{Tools.humanbits(total_bps)}/s{cl.RESET}'))

        cls()
        print(tabulate(
            tabulate_text,
            headers=[f'{cl.BLUE}Ціль', 'Порт', 'Метод', 'Запити', f'Трафік{cl.RESET}'],
            tablefmt='fancy_grid'
        ))
        print_banner(use_my_ip)
    else:
        logger.info(
            f'{cl.GREEN}Усього:{cl.YELLOW} Запити:{cl.GREEN} %s/s,{cl.YELLOW} Трафік:{cl.GREEN} %s/s{cl.RESET}' %
            (
                Tools.humanformat(total_pps),
                Tools.humanbits(total_bps),
            )
        )

    print_progress(time_left, proxies_cnt, use_my_ip)


def print_progress(time_left, proxies_cnt, use_my_ip):
    logger.info(f'{cl.YELLOW}Новий цикл через: {cl.BLUE}{time_left} секунд{cl.RESET}')
    if proxies_cnt:
        logger.info(f'{cl.YELLOW}Кількість проксі: {cl.BLUE}{proxies_cnt}{cl.RESET}')
        if use_my_ip:
            logger.info(f'{cl.YELLOW}Атака також використовує {cl.MAGENTA}ваш IP разом з проксі{cl.RESET}')
    else:
        logger.info(f'{cl.YELLOW}Атака {cl.MAGENTA}без проксі{cl.YELLOW} - використовується тільки ваш IP{cl.RESET}')


def print_banner(use_my_ip):
    print(f'''
- {cl.YELLOW}Навантаження (кількість потоків){cl.RESET} - параметр `-t 3000`, за замовчуванням - CPU * {THREADS_PER_CORE}
- {cl.YELLOW}Статистика у вигляді таблиці або тексту{cl.RESET} - прапорець `--table` або `--debug`
- {cl.YELLOW}Повна документація{cl.RESET} - https://github.com/porthole-ascend-cinnamon/mhddos_proxy
    ''')

    if not use_my_ip:
        print(
            f'        {cl.MAGENTA}Використовувати свій IP або VPN {cl.YELLOW}на додачу до проксі - прапорець `--vpn`{cl.RESET}\n')
