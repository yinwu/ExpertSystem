from django.core.management.base import BaseCommand, CommandError

from experts.models import *
from ExpertSystem.settings import BASE_DIR

class Command(BaseCommand):
    def handle(self, *args, **option):
        print("******start to import test data******")
        with open(BASE_DIR+"/media/"+"experts_test_data") as f:
            content = f.readlines()
            for line in content:
                item = line.split(" ")
                expert = Expert.objects.filter(name=item[0])
                if expert.count() != 0:
                    expert = expert[0]
                    expert.phone = item[1]
                    expert.email = item[2]
                    expert.address = item[3]
                    expert.unit = item[4]
                    expert.degree = item[5]
                    expert.program_type = item[6]
                    expert.level = item[7]
                    expert.save()
                    print("update exist expert:", item[0])
                else:
                    new_expert = Expert()
                    new_expert.name = item[0]
                    new_expert.phone = item[1]
                    new_expert.email = item[2]
                    new_expert.address = item[3]
                    new_expert.unit = item[4]
                    new_expert.degree = item[5]
                    new_expert.program_type = item[6]
                    new_expert.level = item[7]
                    new_expert.save()
                    print("add new expert:", item[0])

        print("******end to import test data******")