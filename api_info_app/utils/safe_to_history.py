from history_app.models import History
from django.core.cache import cache


def safe_to_history(ip, user_id):
    cache.delete("serialized_history")
    new_record = History()
    new_record.ip_address = ip
    new_record.user_id = user_id

    try:
        new_record.save()
    except Exception as e:
        return {"save_to_history ": "ERROR!!! " + str(e), }
    return {"save_to_history": "Success", }
