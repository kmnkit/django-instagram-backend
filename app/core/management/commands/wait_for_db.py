"""
Django command to wait for the database to be available.
"""

import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write("DB를 기다리는 중입니다...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("DB가 아직 초기화되지 않았습니다, 1초 더 기다립니다...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("DB가 준비되었습니다!"))
