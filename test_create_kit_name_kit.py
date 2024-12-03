import sender_stand_request

def positive_assert(test_name):
    kit_body = sender_stand_request.get_kit_body(test_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == test_name

def negative_assert_code_400(test_name):
    kit_body = sender_stand_request.get_kit_body(test_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400

def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert('a')

def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(
        'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')

def test_create_kit_0_letter_in_name_get_failure_response():
    negative_assert_code_400('')

def test_create_kit_512_letter_in_name_get_failure_response():
    negative_assert_code_400(
        'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')

def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert('QWErty')

def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert('Мария')

def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert('"№%@",')

def test_create_kit_space_in_name_get_success_response():
    positive_assert(' Человек и КО ')

def test_create_kit_number_in_name_get_success_response():
    positive_assert('123')

def test_create_kit_without_name_get_failure_response():
    kit_body = {
    }
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400

def test_create_kit_invalid_type_in_name_get_failure_response():
    negative_assert_code_400(123)