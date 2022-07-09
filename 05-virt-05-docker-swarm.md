# Домашнее задание к занятию "5.5. Оркестрация кластером Docker контейнеров на примере Docker Swarm"

## Задача 1

Дайте письменые ответы на следующие вопросы:

- В чём отличие режимов работы сервисов в Docker Swarm кластере: replication и global?
replication - указываем какое количество реплик (копий) приложения будет запущенно в кластере
global - запускает одну таску на каждой ноде кластера.
- Какой алгоритм выбора лидера используется в Docker Swarm кластере?
используется так называемый алгоритм поддержания распределенного консенсуса — Raft.
- Что такое Overlay Network?
общий случай логической сети, создаваемой поверх другой сети. Узлы оверлейной сети могут быть связаны либо физическим соединением, либо логическим, для которого в основной сети существуют один или несколько соответствующих маршрутов из физических соединений. Примерами оверлеев являются сети VPN и одноранговые сети, которые работают на основе интернета и представляют из себя «надстройки» над классическими сетевыми протоколами, предоставляя широкие возможности, изначально не предусмотренные разработчиками основных протоколов.

## Задача 2

Создать ваш первый Docker Swarm кластер в Яндекс.Облаке

Для получения зачета, вам необходимо предоставить скриншот из терминала (консоли), с выводом команды:
```
[root@node01 ~]# docker node ls
ID                            HOSTNAME                STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
rqmk4lwepmqep4w8i1afr2k0l *   node01.netology.cloud   Ready     Active         Leader           20.10.17
rmehd405j1vw1f0ey1ksisjl6     node02.netology.cloud   Ready     Active                          20.10.17
[root@node01 ~]#
```

## Задача 3

Создать ваш первый, готовый к боевой эксплуатации кластер мониторинга, состоящий из стека микросервисов.

Для получения зачета, вам необходимо предоставить скриншот из терминала (консоли), с выводом команды:
```
[root@node01 ~]# docker service ls
ID             NAME                                MODE         REPLICAS   IMAGE                                          PORTS
i2zqv6bcjyet   swarm_monitoring_alertmanager       replicated   1/1        stefanprodan/swarmprom-alertmanager:v0.14.0
5mus0668mdrr   swarm_monitoring_caddy              replicated   1/1        stefanprodan/caddy:latest                      *:3000->3000/tcp, *:9090->9090/tcp, *:9093-9094->9093-9094/tcp
tix95n3obj8w   swarm_monitoring_cadvisor           global       6/6        google/cadvisor:latest
47fw854xvhcn   swarm_monitoring_dockerd-exporter   global       6/6        stefanprodan/caddy:latest
mldspkf1tlwb   swarm_monitoring_grafana            replicated   1/1        stefanprodan/swarmprom-grafana:5.3.4
5hdl35uablru   swarm_monitoring_node-exporter      global       6/6        stefanprodan/swarmprom-node-exporter:v0.16.0
y6tkqqc2ac2f   swarm_monitoring_prometheus         replicated   1/1        stefanprodan/swarmprom-prometheus:v2.5.0
0370b51zincu   swarm_monitoring_unsee              replicated   1/1        cloudflare/unsee:v0.8.0
```

## Задача 4 (*)

Выполнить на лидере Docker Swarm кластера команду (указанную ниже) и дать письменное описание её функционала, что она делает и зачем она нужна:
```
# см.документацию: https://docs.docker.com/engine/swarm/swarm_manager_locking/

root@node01 ~]# docker node list
ID                            HOSTNAME             STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
wnw68wtuhksbxnsm0sjlwhxmm *   node01.netology.yc   Ready     Active         Leader           20.10.17
jjtnqmzdz8mvqdxacowkt54e7     node02.netology.yc   Ready     Active         Reachable        20.10.17
wriryuyrttszu4iexeb6k82da     node03.netology.yc   Ready     Active         Reachable        20.10.17
o6yndm0k4kteor982ip7yepsx     node04.netology.yc   Ready     Active                          20.10.17
x2ufoat42kebqqwuhnd6rq2bl     node05.netology.yc   Ready     Active                          20.10.17
a9n0er4m2fixvjumpeajp1mnq     node06.netology.yc   Ready     Active                          20.10.17

# Включаем автоматическую блокировку существующего класстера для защиты ключа шифрования TLS. Он используется для  связи между узлами swarm, a также для шифрования и дешифрования журналов Raft на диске.
[root@node01 ~]# docker swarm update --autolock=true
Swarm updated.
To unlock a swarm manager after it restarts, run the `docker swarm unlock`
command and provide the following key:

    SWMKEY-1-cXExrG9e6XQqg6nx0eNemZe87CaDPOHGEmbkhJe83rw

Please remember to store this key in a password manager, since without it you
will not be able to restart the manager.

```

