Д/З 1
-Создайте новый Django-проект, подключите DRF в настройках проекта.

-Создайте следующие модели:
 -Пользователь:
  -все поля от обычного пользователя, но авторизацию заменить на email;
  -телефон;
  -город; 
  -аватарка.
   Модель пользователя разместите в приложении users
 -Курс:
  -название,
  -превью (картинка),
  -описание.
 -Урок:
  -название,
  -описание,
  -превью (картинка),
  -ссылка на видео.
 Урок и курс - это связанные между собой сущности. Уроки складываются в курс, в одном курсе может быть много уроков. Реализуйте связь между ними.
 Модель курса и урока разместите в отдельном приложении. Название для приложения выбирайте такое, чтобы оно описывало то, с какими сущностями приложение работает. Например, lms или materials - отличные варианты. 

-Опишите CRUD для моделей курса и урока. Для реализации CRUD для курса используйте Viewsets, а для урока - Generic-классы.
 Для работы контроллеров опишите простейшие сериализаторы.
 При реализации CRUD для уроков реализуйте все необходимые операции (получение списка, получение одной сущности, создание, изменение и удаление).
 Для работы контроллеров опишите простейшие сериализаторы.
 Работу каждого эндпоинта необходимо проверять с помощью Postman.
 Также на данном этапе работы мы не заботимся о безопасности и не закрываем от редактирования объекты и модели даже самой простой авторизацией.

Д/З 2
-Для модели курса добавьте в сериализатор поле вывода количества уроков. Поле реализуйте с помощью SerializerMethodField()

-Добавьте новую модель в приложение users:
 Платежи
 -пользователь,
 -дата оплаты,
 -оплаченный курс или урок,
 -сумма оплаты,
 -способ оплаты: наличные или перевод на счет.
 Поля пользователь, оплаченный курс и отдельно оплаченный урок должны быть ссылками на соответствующие модели.
 Запишите в таблицу, соответствующую этой модели данные через инструмент фикстур или кастомную команду.

-Для сериализатора для модели курса реализуйте поле вывода уроков. Вывод реализуйте с помощью сериализатора для связанной модели.
 Один сериализатор должен выдавать и количество уроков курса и информацию по всем урокам курса одновременно.

-Настроить фильтрацию для эндпоинта вывода списка платежей с возможностями:
 -менять порядок сортировки по дате оплаты,
 -фильтровать по курсу или уроку,
 -фильтровать по способу оплаты.

Д/З 3
-Реализуйте CRUD для пользователей, в том числе регистрацию пользователей, настройте в проекте использование JWT-авторизации и закройте каждый эндпоинт авторизацией.
 Эндпоинты для авторизации и регистрации должны остаться доступны для неавторизованных пользователей.

-Заведите группу модераторов и опишите для нее права работы с любыми уроками и курсами, но без возможности их удалять и создавать новые. Заложите функционал такой проверки в контроллеры.

-Опишите права доступа для объектов таким образом, чтобы пользователи, которые не входят в группу модераторов, могли видеть, редактировать и удалять только свои курсы и уроки.

Д/З 4
-Для сохранения уроков и курсов реализуйте дополнительную проверку на отсутствие в материалах ссылок на сторонние ресурсы, кроме youtube.com.

-Добавьте модель подписки на обновления курса для пользователя. Модель подписки должна содержать следующие поля: «пользователь» (FK на модель пользователя), «курс» (FK на модель курса). Можете дополнительно расширить модель при необходимости.

-Реализуйте пагинацию для вывода всех уроков и курсов.

-Напишите тесты, которые будут проверять корректность работы CRUD уроков и функционал работы подписки на обновления курса.

Д/З 5
-Подключить и настроить вывод документации для проекта. Убедиться, что каждый из реализованных эндпоинтов описан в документации верно, при необходимости описать вручную.

-Подключить возможность оплаты курсов через https://stripe.com/docs/api.
 Доступы можно получить напрямую из документации, а также пройти простую регистрацию по адресу https://dashboard.stripe.com/register.

Д/З 6
-Настройте проект для работы с Celery. Также настройте приложение на работу с celery-beat для выполнения периодических задач.

-Ранее вы реализовали функционал подписки на обновление курсов. Теперь добавьте асинхронную рассылку писем пользователям об обновлении материалов курса.

-С помощью celery-beat реализуйте фоновую задачу, которая будет проверять пользователей по дате последнего входа по полю 
last_login и, если пользователь не заходил более месяца, блокировать его с помощью флага is_active.