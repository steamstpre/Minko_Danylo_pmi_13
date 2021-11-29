from Collection import Collection
from VaccinationPointRequest import VaccinationPointRequest
from Validation import Validation

our_collection = Collection()

our_collection.read_json("data_base.json")
our_collection.most_popular_point()
our_obj = VaccinationPointRequest()
our_collection.append(our_obj)
our_collection.most_popular_hour()
our_collection.print()