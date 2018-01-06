class PrettyEvents:
    def __init__(self):
        pass

    def cast_flags(self, flag):
        return flag

    def cast_extra_fields(self, extra_fields):
        return extra_fields

    def __call__(self, response):
        event_code = response[0]
        out = {"event_code": event_code}
        # pprint(response)

        if event_code == 1:
            out = {
                "_event_name": "flags_replace",
                "message_id": response[1],
                "flags": self.cast_flags(response[2]),
                "extra_fields": self.cast_extra_fields(response[3])
            }
        elif event_code == 2:
            out = {
                "_event_name": "flags_install",
                "message_id": response[1],
                "mask": response[2],
                "extra_fields": self.cast_extra_fields(response[3])
            }
        elif event_code == 3:
            out = {
                "_event_name": "flags_reset",
                "message_id": response[1],
                "mask": response[2],
                "extra_fields": self.cast_extra_fields(response[3])
            }
        elif event_code == 4:
            out = {
                "_event_name": "message_new",
                "message_id": response[1],
                "flags": self.cast_flags(response[2]),
                "extra_fields": self.cast_extra_fields(response[3])
            }
        elif event_code == 5:
            out = {
                "_event_name": "message_edit",
                "message_id": response[1],
                "mask": response[2],
                "peer_id": response[3],
                "timestamp": response[4],
                "new_text": response[5],
                "attachments": response[6]
            }
        elif event_code == 6:
            out = {
                "_event_name": "all_incoming_is_readed",
                "peer_id": response[1],
                "local_id": response[2]
            }
        elif event_code == 7:
            out = {
                "_event_name": "all_outgoing_is_readed",
                "peer_id": response[1],
                "local_id": response[2]
            }
        elif event_code == 13:
            out = {
                "_event_name": "message_deleted",
                "peer_id": response[1],
                "local_id": response[2]
            }
        elif event_code == 14:
            out = {
                "_event_name": "message_restored",
                "peer_id": response[1],
                "local_id": response[2]
            }
        elif event_code == 51:
            out = {
                "_event_name": "chat_edited",
                "chat_id": response[1],
                "self": response[2]
            }
        elif event_code == 61:
            out = {
                "_event_name": "typing_dialog",
                "user_id": response[1],
                "flags": response[2]
            }
        elif event_code == 62:
            out = {
                "_event_name": "typing_chat",
                "user_id": response[1],
                "chat_id": response[2]
            }
        elif event_code == 70:
            out = {
                "_event_name": "call_ended",
                "user_id": response[1],
                "call_id": response[2]
            }
        elif event_code == 80:
            out = {
                "_event_name": "messages_counter",
                "count": response[1],
            }
        elif event_code == 101:
            out = {
                "_event_name": "message",
                "data": response[1],
            }
        elif event_code == 114:
            out = {
                "_event_name": "notifications_settings_edited",
                "peer_id": response[1],
                "sound": response[2],
                "disabled_until": response[3]
            }

        return out
