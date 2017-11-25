# tests of saving the objects and datbase in json format.

import pytest

from mailroom import model

# we'll run these again when the json_save stuff in is.
# pytestmark = pytest.mark.skipif(True, reason="don't have json_save yet")


def test_donor_round_trip():
    # get an arbitrary
    donor = model.get_sample_data()[0]

    json_dict = donor.to_json_compat()

    donor2 = model.Donor.from_json_dict(json_dict)

    print(json_dict)

    print(donor)
    print(donor2)

    assert donor2 == donor

    # in case equality isn't right...
    assert donor.name == donor2.name
    assert donor.norm_name == donor2.norm_name
    assert donor.donations == donor2.donations


def test_database_save():
    db = model.DonorDB(model.get_sample_data())

    json_dict = db.to_json_compat()

    db2 = model.DonorDB.from_json_dict(json_dict)

    print(db2)

    assert db2 == db
    assert db2.donor_data == db.donor_data


def test_save_load_file():
    db = model.DonorDB(model.get_sample_data())
    db.save_to_file("test.json")
    db2 = model.DonorDB.load_from_file("test.json")

    assert db == db2

