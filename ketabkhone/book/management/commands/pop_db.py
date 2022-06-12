from django.core.management.base import BaseCommand
from extra.models import Publisher
from author.models import Author
from loan.models import Debt
from accounting.models import CustomUser
from extra.models import Category
from book.models import Book
from loan.models import Loan
from django.contrib.auth.models import User
# from faker import Faker


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        # import models
        # publisher_obj = User.objects.create_user(felna)
        # Books.objects.create(publoisher=publisher_obj, ...)
        # ba olaviat object besazim
        # fake= Faker()
        # fake.name()
        Publisher1 = Publisher.objects.create(
            name="ahmadreza", addres="khone baghalei")
        Author1 = Author.objects.create(
            name="Authoremoon", description="ye marde kheily khoob!!")
        Debt1 = Debt.objects.create(amount=80)
        cate1 = Category.objects.create(name="alireza.sh")
        user_obj = User.objects.create_user(
            username="ab12345fdj", password="ab22ghfrd")
        user1 = CustomUser.objects.create(age=20, phone_number="09126234567", gender="M",
                                          addres="null addres", nationalcode="0345678901", user=user_obj, Debt=Debt1)
        loan_obj = Loan.objects.create(user=user1, status="C")
        book_obj = Book.objects.create(name="test_book2", desk="null desk", poblisher=Publisher1,
                                       translator="mr.translator", user=user1, active=True, loan=loan_obj)
        book_obj.category.add(cate1)
        book_obj.author.add(Author1)
        # pic = models.FileField(upload_to='team_icons', null='True', blank='True',
        #                               default='settings.MEDIA_ROOT/pictures/picture.png')
        # book_obj.cover.add(pic)
        book_obj.save()
        # book | many to many --> category, author | foreignkey --> publisher
        print("ok !")
        for i in range(5):
            print(i)
        self.stdout.write("123")


# orm
# object renational make_password
# crut query set
#
