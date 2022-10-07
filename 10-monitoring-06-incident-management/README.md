Краткое описание инцидента:
    В 22:52 (21.10) по UTC на нескольких сервисах GitHub.com пострадали несколько сетевых разделов и последующим сбоем базы данных, что привело к появлению непоследовательной информации на нашем веб-сайте.


Предшествующие события:
    Попытка повысить производительность сервиса.
    

Причина инцидента:
    плановые работы по техническому обслуживанию по замене вышедшего из строя оптического оборудования 100G привели к потере связи между нашим сетевым центром на восточном побережье США и нашим основным центром обработки данных на восточном побережье США.

Воздействие:
    обслуживание ухудшилось на 24 часа 11 минут были затронуты несколько внутренних систем, в результате чего сервис отображал устаревшую и непоследовательную информацию. 

Обнаружение:
   Инцидент был замечен дежурным инженером. Затем были привлечены ответственные 
разработчики. 


Реакция:
    Ответственные разработчики восстановли cвязь за 43 секунды.


Таймлайн:
    21 октября 22:52  Orchestrator, который был активен в основном центре обработки данных, начал процесс отмены выбора руководства.
    21 октября 22:54 системы мониторинга начали генерировать предупреждения, указывающие на то, что системах возникло множество неисправностей.
    21 октября 23:07 команда разработчиков  вручную заблокировла внутренние инструменты развертывания, чтобы предотвратить внесение каких-либо дополнительных изменений
    21 октября 23:13 Были вызваны дополнительные инженеры из группы разработки баз данных.
    21 Октября 23:19 остановка выполнение заданий, которые записывают метаданные о таких вещах, как push
    22 октября 00:05 разработка плана по устранению несоответствий данных и реализации процедур аварийного переключения для MySQL
    22 октября 00:41 запущен процесс резервного копирования всех затронутых кластеров MySQL
    22 октября 11:12 Все первичные базы данных снова установлены на Восточном побережье США
    22 октября 16:24 реплики были синхронизированы, выполнeно аварийное переключение на исходную топологию
    22 октябрь 23:03 система заработала в штатном режиме.


Последующие действия:
    Систематическaя практика проверки сценариев сбоев. Эта работа будет включать в себя будущие инвестиции в инструменты инжекции разломов и хаоса на GitHub.

