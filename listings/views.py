from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.response import Response
from rest_framework import status
from listings.tasks import send_booking_confirmation_email

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            booking = Booking.objects.get(pk=response.data['id'])
            user_email = booking.user.email
            listing_title = booking.listing.title
            send_booking_confirmation_email.delay(user_email, listing_title)
        return response
