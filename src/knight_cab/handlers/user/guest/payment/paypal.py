from dotenv import load_dotenv
import paypalrestsdk
import logging
import os

load_dotenv()

paypalrestsdk.configure({
    "mode": os.environ["PAYPAL_MODE"],
    "client_id": os.environ["PAYPAL_CLIENT_ID"],
    "client_secret": os.environ["PAYPAL_CLIENT_SECRET"],})



async def pay_with_paypal(data):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": f"https://t.me/knight_club_bot",
            "cancel_url": "https://t.me/knight_club_bot"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "item",
                    "sku": "item",
                    "price": "1",
                    "currency": "USD",
                    "quantity": 1}]},
            "amount": {
                "total": "1",
                "currency": "USD"},
            "description": "This is a donation transaction made for CSEC-ASTU."}]})

    if payment.create():
        logging.info("Payment created successfully")
    else:
        logging.error(payment.error)

    for link in payment.links:
        print(link)
        if link.rel == "approval_url":
            approval_url = str(link.href)
            print(approval_url)
            pay_id = approval_url.split('=')[-1]
        if link.rel == 'self':
            paypal_id_link = link.href
            paypal_transaction_id = paypal_id_link.split('/')[-1]
            print(paypal_transaction_id)
            try:
                payment = paypalrestsdk.Payment.find(paypal_transaction_id)
                print(payment['state'])
            except Exception as e:
                print(e)
    payment_history = paypalrestsdk.Payment.all()

    # List
    logging.info("List Payment:")
    for payment in payment_history.payments:
        logging.info("  -> Payment[%s]" % (payment.id))
        payment = paypalrestsdk.Payment.find(payment.id)
        # print(payment)
    return {'status_url': f'https://www.paypal.com/checkoutnow?token={pay_id}',
            'txn_id': paypal_transaction_id,
            'error': 'ok',
            'amount': 1}
