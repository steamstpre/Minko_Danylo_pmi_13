from Validation import Validation

class VaccinationPointRequest(object):
    def __init__(self , id_input = 0 , point_input = "none" , time_input = 10 , date_input = "2020-03-23" , name_input = "name"):
        self._id = id_input
        self._point = point_input
        self._time = time_input
        self._date = date_input
        self._name = name_input

    @property
    def id(self):
        return self._id

    @property
    def point(self):
        return self._point

    @property
    def time(self):
        return self._time

    @property
    def date(self):
        return self._date

    @property
    def name(self):
        return self._name

    @point.setter
    @Validation.check_point
    def point(self, value):
        self._point = value

    @time.setter
    @Validation.check_time
    def time(self, value):
        self._time = value

    @date.setter
    @Validation.check_date
    def date(self, value):
        self._date = value

    @name.setter
    @Validation.check_name
    def name(self, value):
        self._name = value

    @id.setter
    def id(self , value):
        self._id = value

    def set_from_file(self , **arr):
        for (field, value) in arr.items():
            setattr(self, field, value)

    def __get_dictionary(self):
        return dict((name, getattr(self, name)) for name in dir(self) if
                    not name.startswith('_'))

    def __str__(self):
        return "Company:" + '\n'.join("%s : %r" % (key, str(val)) for (key, val)
                                      in self.__get_dictionary().items()) + " "
