# Create Token
# Create Booking ID
# Update the booking (Put) - Booking ID, Token
# Delete the booking

# Verify that created booking id can be updated and deleted.
# fixtures will be used to pass the data


import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


class TestCrudBooking(object):

    @allure.title("Verify that booking can be updated")
    @allure.description("Verify that full update on a booking with a booking id and token is working")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = put_requests(url=put_url,
                                headers=Util.common_headers_put_delete_patch_cookie(token=token),
                                payload=payload_create_booking(),
                                auth=None,
                                in_json=False)
        verify_http_status_code(response_data=response, expect_data=200)

    @allure.title("Verify that booking can be deleted")
    @allure.description("Verify that delete booking operation is working using "
                        "a booking id and token")
    def test_delete_booking_id(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        del_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = delete_requests(url=del_url,
                                   headers=Util.common_headers_put_delete_patch_cookie(token=token),
                                   auth=None,
                                   in_json=False)
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data=response, expect_data=201)
