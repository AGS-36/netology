# **Домашнее задание к занятию "3.6. Компьютерные сети, лекция 1"**

# Работа c HTTP через телнет. 

```
[vagrant@otuslinux ~]$ telnet stackoverflow.com 80
Trying 151.101.129.69...
Connected to stackoverflow.com.
Escape character is '^]'.
GET /questions HTTP/1.0
HOST: stackoverflow.com

HTTP/1.1 301 Moved Permanently
cache-control: no-cache, no-store, must-revalidate
location: https://stackoverflow.com/questions
x-request-guid: ca5a0e9c-2439-4f41-b78e-1e867e874f45
feature-policy: microphone 'none'; speaker 'none'
content-security-policy: upgrade-insecure-requests; frame-ancestors 'self' https://stackexchange.com
Accept-Ranges: bytes
Date: Mon, 23 May 2022 21:39:37 GMT
Via: 1.1 varnish
Connection: close
X-Served-By: cache-fra19177-FRA
X-Cache: MISS
X-Cache-Hits: 0
X-Timer: S1653341978.565907,VS0,VE92
Vary: Fastly-SSL
X-DNS-Prefetch-Control: off
Set-Cookie: prov=e41a4d17-596d-d2b9-1ce4-65cf2d86b55e; domain=.stackoverflow.com; expires=Fri, 01-Jan-2055 00:00:00 GMT; path=/; HttpOnly

Connection closed by foreign host.

Код состояния HTTP 301 или Moved Permanently (с англ. — «Перемещено навсегда») — стандартный код ответа HTTP, получаемый в ответ от сервера в ситуации, когда запрошенный ресурс был на постоянной основе перемещён в новое месторасположение, и указывающий на то, что текущие ссылки, использующие данный URL, должны быть обновлены. Адрес нового месторасположения ресурса указывается в поле Location получаемого в ответ заголовка пакета протокола HTTP.
```

# Повторение задания в браузере
```
Код ответа 301 
Время загрузки - Finish: 6.72 s 
Самый долгий запрос - Request URL: https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js - 5.32 s
```
https://github.com/AGS-36/netology/blob/master/headers.png
# Какой IP адрес у вас в интернете?

```
[vagrant@otuslinux ~]$  wget -qO- eth0.me
95.32.186.136
```

# Какому провайдеру принадлежит ваш IP адрес? Какой автономной системе AS? Воспользуйтесь утилитой whois

```
Провайдер: Ростелеком
Название сети: MACROREGIONAL_CENTER
AS12389

inetnum:        95.32.128.0 - 95.32.255.255
netname:        MACROREGIONAL_CENTER
descr:          Regional multiservice network access
descr:          xDSL dynamic ip pool
descr:          OJSC Rostelecom, Voronezh branch
descr:          35, Revolutsii prosp.
descr:          Voronezh,394000
descr:          Russia
descr:          ex-netname: VSI-DSL-ACCESS
country:        RU
...
...
```

# Через какие сети проходит пакет, отправленный с вашего компьютера на адрес 8.8.8.8? Через какие AS? Воспользуйтесь утилитой traceroute
```
traceroute -An 8.8.8.8
origin:     AS12389
origin:     AS15169
```

# Повторите задание 5 в утилите mtr. На каком участке наибольшая задержка - delay?  
```
Keys:  Help   Display mode   Restart statistics   Order of fields   quit
                                                                             Packets               Pings
 Host                                                                      Drop   Rcv    Avg Gmean Jttr Javg Jmax Jint
 1. AS???   10.0.2.2                                                          0   243    0.6   0.6  0.4  0.1  0.7  1.9
 2. AS???   192.168.1.1                                                       0   243	4.0   3.8  0.0  1.5 12.0 21.9
 3. AS???   100.103.0.1                                                       0   243   34.6  34.2  1.9  4.1 42.7 47.5
 4. AS12389 213.59.232.208                                                    0   243   33.4  33.2  0.7	2.2 36.4 27.7
 5. AS12389 87.226.146.73                                                     0   243	35.1  34.6  3.2  4.1 75.9 124.
 6. AS12389 87.226.146.68                                                     0   243	34.0  33.8  1.1  2.7 26.5 23.8
 7. AS12389 185.140.148.155                                                  86   157   61.4  48.3 2235 15.5 2235 2253
 8. AS15169 72.14.205.132                                                     0   243   47.8  47.8  4.5	1.6 15.8 44.0
 9. AS15169 108.170.250.129                                                   0   243	48.1  48.0  0.6  1.7 18.7 30.6
10. AS15169 108.170.250.146                                                   0   243	66.4  49.7 4183 38.6 4186 8145
11. AS15169 142.250.239.64                                                    0   243	61.7  61.5  0.3	3.6 31.3 60.2
12. AS15169 172.253.66.110                                                    0   243	62.8  62.8 16.8  1.9 21.1 36.9
13. AS15169 172.253.51.185                                                    0   243   64.4  64.2  2.8	2.5 73.8 23.3
14. ???
```
# Наибольшая задержка на 13 участке.

# Какие DNS сервера отвечают за доменное имя dns.google? Какие A записи? воспользуйтесь утилитой dig 
```
dns.google.		753	IN	A	8.8.8.8
dns.google.		753	IN	A	8.8.4.4
8.8.8.8
8.8.4.4
```

# Проверьте PTR записи для IP адресов из задания 7. Какое доменное имя привязано к IP? воспользуйтесь утилитой dig 
```
8.8.8.8.in-addr.arpa.	78967	IN	PTR	dns.google.
4.4.8.8.in-addr.arpa.	82112	IN	PTR	dns.google.
```
