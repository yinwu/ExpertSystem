from django.core.management.base import BaseCommand, CommandError

from experts.models import *
from ExpertSystem.settings import BASE_DIR
from django.contrib.auth.models import User, Group
from django.contrib.auth.hashers import make_password


def add_user(expert):
    new_expert_phone = expert.phone
    print("username: ", new_expert_phone)
    new_user = User.objects.create_user(username=new_expert_phone, password=new_expert_phone, email=expert.email)
    new_user.is_staff = True
    new_user.is_active = True
    new_user.save()

    # user_group = Group.objects.get(id=2)
    # new_user = User.objects.get(username=new_expert_phone)
    # new_user.groups.add(user_group)
    expert.account = new_user
    expert.save()
    print("用户创建成功 " + str(expert.phone))

def update_user(expert, new_value):
    if new_value[1] != expert.phone:
        try:
            user = User.objects.get(username = expert.phone)
            user.username = new_value
            user.password = new_value
            user.save()
        except:
            print("更新用户账户信息失败")
    else:
        user = User.objects.get(username = expert.phone)
        user.is_staff = True
        user.save()


class Command(BaseCommand):
    def handle(self, *args, **option):
        print("******start to import test data******")
        with open(BASE_DIR+"/media/"+"experts_test_data") as f:
            content = f.readlines()
            for line in content:
                item = line.split(" ")
                experts = Expert.objects.filter(name=item[0])
                if experts.count() != 0:
                    expert = experts[0]
                    #update_user(expert, item)
                    expert.phone = item[1]
                    expert.email = item[2]
                    expert.address = item[3]
                    expert.unit = item[4]
                    expert.degree = item[5]
                    expert.program_type = item[6]
                    expert.level = item[7]
                    expert.save()
                    add_user(expert)
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
                    add_user(new_expert)

        print("******end to import test data******")