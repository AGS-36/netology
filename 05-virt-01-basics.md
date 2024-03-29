# **Задача 1**

Полная (аппаратная) виртуализация.
Гипервизоры первого типа работают на аппаратном уровне без необходимости установки какой-либо ОС на хост. Они сами
являются ОС.

Паравиртуализация.
Гипервизорам второго типа необходима ОС для доступа монитора виртуальных машин (гипервизора) к аппаратным
ресурсам хоста. Паравиртуализация разделяет процесс с гостевой операционной системой. Этот метод использует гипервизор для разделения доступа к основным аппаратным средствам, но объединяет код, касающийся виртуализации.
При применении паравиртуализации нет необходимости эмулировать аппаратное обеспечение, более того, гостевая ОС и гипервизор используют общий набор драйверов, что выгодно отличает эту технологию от эмуляции устройств, когда гостевая ОС и гипервизор используют различные драйверы.  До недавних пор основным недостатком паравиртуализации являлась необходимость модификации кода ОС, однако, с появлением аппаратной поддержки виртуализации, такой как Intel VT и AMD-V, стало возможным выполнение любых ОС без модификации ядра.

Виртуализация уровня операционной системы.
Виртуализация ресурсов на уровне ОС обеспечивает разделение одного физического сервера на несколько защищенных виртуализированных частей (контейнеров), каждая из которых представляется для владельца как один сервер. Виртуальная машина представляет собой окружение для приложений, запускаемых изолированно. При этом виртуальные контейнеры, работающие на уровне ядра ОС, крайне мало теряют в быстродействии  по сравнению с производительностью «реального» сервера, что позволяет запускать в рамках одного физического хоста десятки и сотни виртуальных контейнеров. Однако существуют определенные ограничения по запуску виртуальных машин с разными версиями ядра ОС.  Вышеперечисленные преимущества делают виртуализацию уровня операционной системы наиболее применимой при оказании хостинг-услуг, когда в рамках одного сервера  необходимо организовать множество однотипных изолированных друг от друга виртуальных машин.

# **Задача 2**

физические сервера -  высоконагруженная база данных, чувствительная к отказу. Системы, выполняющие высокопроизводительные расчеты на GPU. Чтобы добиться максимальной производительности и не тратить ресурсы на гипервизор.
Виртуализация уровня операционной системы - Различные web-приложения, если хостовая система из семейства linux, если хостовая система windows, то выбрал бы паравиртуализацию. 
виртуализация уровня ОС - Windows системы для использования Бухгалтерским отделом 
Виртуализация уровня ОС - Системы, выполняющие высокопроизводительные расчеты на GPU, чтобы отказаться от гипервизора.


# **Задача 3**

100 виртуальных машин на базе Linux и Windows, общие задачи, нет особых требований
Преимущественно Windows based инфраструктура, требуется реализация программных балансировщиков нагрузки, репликации данных и автоматизированного механизма создания резервных копий Думаю для этой задачи подойдет VMWare, думаю что получится выиграть в производительности, относительно других продуктов.
Требуется наиболее производительное бесплатное opensource решение для виртуализации небольшой (20 серверов) инфраструктуры Linux и Windows виртуальных машин Т.к. требуется opensourse решение, то думаю что следует использовать KWM или Xen
Необходимо бесплатное, максимально совместимое и производительное решение для виртуализации Windows инфраструктуры Думаю, что тут подойдет Hyper-V т.к. он бесплатен и разработан microsoft.
Необходимо рабочее окружение для тестирование программного продукта на нескольких дистрибутивах Linux Думаю, что для этой цели подойдет что-нибудь из беслатного ПО (KWM, Xen, Virtual box), а не использовать их платные аналоги.


# **Задача 4**

Т.к. разные системы виртуализации имеет свои особенности: архитектуру гипервизора; используемый тип виртуализации; перечень совместимого оборудования; перечень поддерживаемых операционных систем. Эти особенности могут послужить причиной для параллельной эксплуатации нескольких виртуальных платформ в рамках виртуальной среды одного предприятия. Также гетерогенность возникает в результате развертывания дополнительной виртуальной платформы с целью получения новой функциональности виртуальной среды или снижения стоимости решений виртуализации. Наряду с преимуществами, виртуальная среда дает целый комплекс проблем, связанных с обеспечением безопасности информационных систем. Виртуальная среда динамична, а существующие средства обеспечения информационной безопасности рассчитаны на статические системы. Автоматизация управления виртуальной средой развита недостаточно и требует существенного человеческого участия. Ошибки в управлении виртуальной средой приводят к нехватке вычислительных ресурсов на физических узлах и могут спровоцировать лавинообразный процесс автоматического перемещения виртуальных машин, сопровождаемый каскадными отключениями физических серверов. Размещенные в виртуальной среде информационные системы наиболее уязвимы к увеличениям нагрузок, вызванных DDoS-атаками злоумышленников, ошибками в программном обеспечении, а также нарушениями правил эксплуатации. В гетерогенной среде эта ситуация усугубляется тем, что необходимо одновременно управлять несколькими виртуальными платформами, а возможности автоматизации управления еще более ограничены совместимостью платформ. Для минимизации этих рисков и проблем не стоит использовать множество систем виртуализации, а также иметь систему мониторинга вычислительных ресурсов в гетерогенной виртуальной среде. Я бы в данный момент не создавал гетерогенную систему из-за нехватки опыта и знаний в этой сфере.


