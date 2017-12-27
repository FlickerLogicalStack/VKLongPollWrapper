# VKLongPollWrapper

Обёртка под long poll сервер вк версии 2.0.

### Использование:
```
>>> raw_event = [3, 460164, 1, 225714708]
>>> pretty_events_instance = PrettyEvents()
>>> casted_event = pretty_events_instance(raw_event)
>>> casted_event
{'_event_name': 'message_flags_reset', 'message_id': 460164, 'mask': 1}
```

Все названия ключей сделаны в соответствии с документацией.

### TODO

* Обработка Attachments
* Разделение событий из сообщества и обычного диалога
* Some configs
* Обработка платформы с маской 64 в режиме long poll
