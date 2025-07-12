#!/usr/bin/env python3
"""
Background task for sending booking confirmation emails.
"""
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(user_email: str, listing_title: str) -> None:
    """
    Sends an email confirming the booking to the user.
    """
    subject = "Booking Confirmation"
    message = f"Thank you for booking: {listing_title}.\nYour booking is confirmed!"
    from_email = None  # Uses DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)
