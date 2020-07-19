from django.core.management.base import BaseCommand, CommandError

from experts.models import *
from ExpertSystem.settings import BASE_DIR
import datetime


class Command(BaseCommand):
    def handle(self, *args, **option):
        print("***** Import program Data start *****")
        with open(BASE_DIR+"/media/"+"program_test_data") as f:
            content = f.readlines()
            for line in content:
                item = line.split(" ")
                print(item)
                try:
                    exist_program = Program.objects.get(seq=item[0])
                    exist_program.name = item[1]
                    exist_program.desp = item[2]
                    exist_program.responser = item[3]
                    exist_program.location = item[4]
                    exist_program.money = item[5]
                    exist_program.save()
                except:
                    new_program = Program()
                    new_program.seq = item[0]
                    new_program.name = item[1]
                    new_program.desp = item[2]
                    new_program.responser = item[3]
                    new_program.location = item[4]
                    new_program.money = item[5]
                    new_program.program_date = datetime.datetime.now().date()
                    new_program.start_date = datetime.datetime.now().date()
                    new_program.end_date = datetime.datetime.now().date()
                    new_program.save()



        print("***** Import program Data end *****")