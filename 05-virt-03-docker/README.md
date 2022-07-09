---

## Задача 1
https://hub.docker.com/layers/246208880/ags36/netology/nginx/images/sha256-2d09cb62bf083ef9900edc4c489b72150c543d5196a523bceac6e72f32dbc5ee?context=repo


## Задача 2

Посмотрите на сценарий ниже и ответьте на вопрос:
"Подходит ли в этом сценарии использование Docker контейнеров или лучше подойдет виртуальная машина, физическая машина? Может быть возможны разные варианты?"

Детально опишите и обоснуйте свой выбор.

--

Сценарий:

- Высоконагруженное монолитное java веб-приложение;
  Тут бы я выбрал ВМ, т.к. java приложения довольно тяжеловесные и требуют определенное колличество ресурсов.
- Nodejs веб-приложение;
  Думаю здесь docer подойдет очень хорошо, т.к. приложение легковесное.
- Мобильное приложение c версиями для Android и iOS;
  Тут думаю стоит использовать только ВМ.
- Шина данных на базе Apache Kafka;
  Думаю тут я бы выбрал ВМ так как Apache Kafka это не легковесное приложение, а требует еще Java зависимости. 
- Elasticsearch кластер для реализации логирования продуктивного веб-приложения - три ноды elasticsearch, два logstash и две ноды kibana;
- Мониторинг-стек на базе Prometheus и Grafana;
  Думаю тут лучше это развернуть на ВМ. Так как он лучше работает на линукс системах, а хостовая система может быть и windows.
- MongoDB, как основное хранилище данных для java-приложения;
  Для базы данных лучше использовать физическую машину.
- Gitlab сервер для реализации CI/CD процессов и приватный (закрытый) Docker Registry.
  Тут я бы использовал физическую или виртуальную машину.

## Задача 3
```
► docker run --name centos -t -v `pwd`/data:/home/data -d centos
106500fca3ceeb4b3f9c6c3295b8c255ef0837f4ffb0160fc51cc3364891288a
► docker run --name debian -t -v `pwd`/data:/home/data -d debian
0a1cef0305413b6b4d4d3f4c1bc044a74c5685f714f411c62efbcbc608428e6c
► docker exec -ti centos bash
[root@106500fca3ce /]# touch /home/data/test.txt
[root@106500fca3ce /]# ls /home/data/test.txt
/home/data/test.txt
► touch test2.txt
► docker exec -ti debian bash
root@0a1cef030541:/# ls /home/data/
test.txt  test2.txt
```

## Задача 4 (*)

https://hub.docker.com/layers/246231557/ags36/netology/ansible/images/sha256-7d5c6065babd336c8565b5dbc51180491624c10aee2864e6e8bb7c7169d25e83?context=repo
---

