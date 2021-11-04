import json
import Validation
from VaccinationPointRequest import VaccinationPointRequest


class Collection:
    def __init__(self, *our_list, state=None):
        self.our_list = list(our_list[:])

    def __getitem__(self, item):
        return self.our_list[item]

    def __len__(self):
        return len(self.our_list)

    def __setitem__(self, key, value):
        self.our_list[key] = value

    def __str__(self):
        return [str(item) for item in self.our_list]

    def check_unical_id(self , id):
        for i in self.our_list:
            if i.id == id:
                raise ValueError

    def check_time(self , time):
        for i in self.our_list:
            try:
                for i in self.our_list:
                    if i.id == time:
                        raise ValueError
                minutes = int(time[3:])
                if minutes % 20 != 0:
                    raise ValueError
            except:
                print("wrong value of time")

    def append(self , item):
        check_status = True
        if self.__len__() != 0:
           try:
               self.check_unical_id(item.id)
               self.check_time(item.time)
           except ValueError:
               print("wrong id or time")
        self.our_list.append(item)

    def read_json(self , path):
         try:
            file_ = open(path , encoding="utf-8")
            file = json.load(file_)
            for i , item in enumerate(file):
                try:
                    our_obj = VaccinationPointRequest()
                    our_obj.set_from_file(**item)
                    self.append(our_obj)
                except ValueError:
                    print("value errorr")
                    continue
                except AttributeError:
                    print("wrong atribute")
                    continue
            file_.close()
         except:
            print("not correct data")

    def write_to_json(self , path):
        with open(path , 'w' , encoding='utf-8') as our_file:
            json.dump([obj.__dict__ for obj in self.our_list], our_file , ensure_ascii=False)
        our_file.close()

    def input_to_obj(self, path):
        our_obj = VaccinationPointRequest()
        try:
            count_of_fileds = int(input("count of fileds: "))
            if count_of_fileds > 5:
                raise ValueError
            for i in range(count_of_fileds):
                field = input("your field: ")
                value = input("your value: ")
                if field == "id":
                    try:
                        self.check_unical_id(value)
                    except ValueError:
                        print("wrong id , please try one more time")
                        return
                if field == "time":
                    try:
                        self.check_time(value)
                    except ValueError:
                        print("wrong time , please try one more time")
                        return
                setattr(our_obj, field, value)
        except:
            print("wrong value")
        self.append(our_obj)
        self.write_to_json(path)

    def most_popular_hour(self):
        our_list_of_unikal = {}
        count_of_same = 0
        for i in self.__len__():
            if self.our_list[i].time[0:2] == self.our_list[i+1].time[0:2]:
                count_of_same += 1
            else:
                for j in our_list_of_unikal:
                    j[self.our_list[i].time[0:2]] = count_of_same

    def most_popular_point(self):
        count_of_forum = 0
        count_of_vG = 0
        count_of_kG = 0
        for i in self.our_list:
            if(i.point == "Forum"):
                count_of_forum += 1
            if(i.point == "VictoryGardens"):
                count_of_vG += 1
            if(i.point == "KingCross"):
                count_of_kG += 1
        return max(count_of_forum ,count_of_vG, count_of_kG)

    def print(self):
        for i in self.our_list:
            print(i.__str__)


