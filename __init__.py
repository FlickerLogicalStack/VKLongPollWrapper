from collections import defaultdict

class PrettyEvents:
	def _cast_flags(self, flag, is_community=False):
		if is_community:
			q = defaultdict(lambda: None,
				{
					1: "IMPORTANT",
					2: "UNANSWERED",
				})
		else:
			q = defaultdict(lambda: None,
				{
					1: "UNREAD",
					2: "OUTBOX",
					4: "REPLIED",
					8: "IMPORTANT",
					16: "CHAT",
					32: "FRIENDS",
					64: "SPAM",
					128: "DELЕTЕD",
					256: "FIXED",
					512: "MEDIA",
					65536: "HIDDEN"
				})

		out = [q[2**int(i)] for i in range(len(bin(flag)[2:][::-1])) if (bin(flag)[2:][::-1][i] == "1" and q[2**int(i)])]

		return out

	def _cast_extra_fields(self, extra_fields):
		out = {}
		q = ["peer_id", "timestamp", "text", "attachments", "random_id"]

		for i in range(len(extra_fields)-1):
			out[q[i]] = extra_fields[i]
		if "peer_id" in out:
			out["peer_id"] = abs(out["peer_id"])

		return out

	def __call__(self, response):
		event_code = response[0]

		if event_code == 1:
			out = {
				"_event_name": "message_flags_replace",
				"message_id": response[1],
				"flags": self._cast_flags(response[2]),
			}
			out.update(self._cast_extra_fields(response[3:]))
		elif event_code == 2:
			out = {
				"_event_name": "message_flags_install",
				"message_id": response[1],
				"mask": response[2],
			}
			out.update(self._cast_extra_fields(response[3:]))
		elif event_code == 3:
			out = {
				"_event_name": "message_flags_reset",
				"message_id": response[1],
				"mask": response[2],
			}
			out.update(self._cast_extra_fields(response[3:]))
		elif event_code == 4:
			out = {
				"_event_name": "message_new",
				"message_id": response[1],
				"flags": self._cast_flags(response[2]),
			}
			out.update(self._cast_extra_fields(response[3:]))
		elif event_code == 5:
			out = {
				"_event_name": "message_edit",
				"message_id": response[1],
				"mask": response[2],
				"peer_id": response[3],
				"timestamp": response[4],
				"new_text": response[5],
			}
			if len(response[1:]) > 5 :
				out["attachments"] = response[6]
		elif event_code == 6:
			out = {
				"_event_name": "messages_in_readed",
				"peer_id": response[1],
				"local_id": response[2]
			}
		elif event_code == 7:
			out = {
				"_event_name": "messages_out_readed",
				"peer_id": response[1],
				"local_id": response[2]
			}
		elif event_code == 8:
			out = {
				"_event_name": "friend_online",
				"user_id": abs(response[1]),
				"timestamp": response[3]
			}
			out.update(self._cast_extra_fields(response[1:-1]))
		elif event_code == 9:
			out = {
				"_event_name": "friend_offline",
				"user_id": abs(response[1]),
				"flags": ["TIMEOUT" if response[2] == 1 else "LOGOUT"],
				"timestamp": response[3]
			}
		elif event_code == 10:
			out = {
				"_event_name": "community_flags_reset",
				"peer_id": response[1],
				"mask": response[2],
			}
		elif event_code == 11:
			out = {
				"_event_name": "community_flags_replace",
				"peer_id": response[1],
				"flags": self._cast_flags(response[2]),
			}
		elif event_code == 12:
			out = {
				"_event_name": "community_flags_install",
				"peer_id": response[1],
				"mask": response[2],
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
		elif event_code == 114:
			out = {
				"_event_name": "notifications_settings_edited",
				"peer_id": response[1],
				"sound": response[2],
				"disabled_until": response[3]
			}
		else:
			out = {
				"_event_code": event_code,
				"data": response[1:]
			}

		return out
