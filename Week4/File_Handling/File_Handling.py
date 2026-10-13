
import csv

from django.db.models.expressions import result


# with open("user_details.csv", "w", newline="") as csv_file:
#     csv_writer = csv.writer(csv_file)
#
#     csv_writer.writerow(["Title", "firstName", "lastName", "gender", "email"])
#
#     csv_writer.writerow(["Honorable", "Alasdair", "Beeckx", "Male", "abeeckx0@un.org"])
#     csv_writer.writerow(["Dr", "Saunder", "Murname", "Male", "smurname1@ftc.gov"])
#     csv_writer.writerow(["Honorable", "Julissa", "Spriddle", "Female", "jspriddle2@chicagotribune.com"])
#     csv_writer.writerow(["Rev", "Bernadene", "Peak", "Female", "bpeak3@fc2.com"])
#     csv_writer.writerow(["Mrs", "Cass", "Bernardeschi", "Male", "cbernardeschi4@technorati.com"])
#     csv_writer.writerow(["Honorable", "Aggi", "Lipson", "Female", "alipson5@ucoz.ru"])
#     csv_writer.writerow(["Ms", "Trescha", "Damato", "Female", "tdamato6@skyrock.com"])
#     csv_writer.writerow(["Dr", "Dav", "Headon", "Male", "dheadon7@ted.com"])
#     csv_writer.writerow(["Honorable", "Nealson", "Janeway", "Male", "njaneway8@360.cn"])
#     csv_writer.writerow(["Mrs", "Laney", "Trobey", "Female", "ltrobey9@eventbrite.com"])
#
# print("File created successfully")

def transform_user_details(csv_file_name):

    try:
        with open("csv_file_name", "r", newline="") as csv_file:
            csv_reader = csv.reader(csv_file)

            # for row in csv_reader:
            #     print(type(row))
            #     print(row)

            new_user_data = []

            # for row in csv_reader:
            #     print(type(row))
            #     print(row)


            for user in csv_reader:
                new_list = []
                new_list.append(user[1])
                new_list.append(user[2])
                new_list.append(user[4])
                new_user_data.append(new_list)

            print(new_user_data)


    except FileNotFoundError:
        print("File not found")

