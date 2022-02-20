import device_module

def test_device_module():
    test = "test_files/device_test.json"
    data = device_module.validate_device_json(test)
    assert data == {'device_id': 1,
                    'patient_assigned': 12,
                    'type': 'temperature',
                    'measurement': 98.6,
                    'MAC': '30-65-EC-6F-C4-58',
                    'purchase_date': '01-01-2001',
                    'model_number': 1234,
                    'model_name': 'temp-o-matic',
                    'serial_number': 56789}
