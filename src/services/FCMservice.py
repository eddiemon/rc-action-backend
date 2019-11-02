from pyfcm import FCMNotification


class FCMService:
    def __init__(self):
        self._push_service = FCMNotification(api_key="<api-key>")

    def send_push_notification(self, message, device_ids, low_priority=False):
        result = self._push_service.notify_multiple_devices(registration_ids=device_ids,
                                                            message_body=message,
                                                            low_priority=low_priority)

        print(result)
