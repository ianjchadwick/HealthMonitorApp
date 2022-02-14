import device_module

def test_device_module():
    test = "test_files/device_test.json"
    data = device_module.device_reading(test)
    assert data == [1, 12, 'temperature', 98.6, '30-65-EC-6F-C4-58', '01-01-2001', 'temp-o-matic', 'temp-o-matic',
                    56789]