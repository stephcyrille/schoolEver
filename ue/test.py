import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Ue


class UeModelTests(TestCase):

    def test_was_published_recently_with_future_ue(self):
        """
        was_published_recently() returns False for ue whose created_at date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_ue = Ue(created_at=time)
        self.assertIs(future_ue.was_published_recently(), False)

    def test_was_published_recently_with_old_ue(self):
        """
        was_published_recently() returns False for ue whose created_at date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_ue = Ue(created_at=time)
        self.assertIs(old_ue.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose created_at date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_ue = Ue(created_at=time)
        self.assertIs(recent_ue.was_published_recently(), True)