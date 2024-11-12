from celery import shared_task

@shared_task
def send_notification(post_author, comment_author, post_title):
    # Simula o envio de uma notificação
    print(f"Notificação: {comment_author} comentou no seu post '{post_title}'.")
