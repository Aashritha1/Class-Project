from django.core.management.base import BaseCommand,CommandError
import click
class Command(BaseCommand):
    help="my secret django"
    def handle(self, *args, **options):
        click.echo(click.style('Hello World!', fg='green'))
