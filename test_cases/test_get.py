import sys
import pytest
import unittest
from request_models.requests_methods import REQ
from helpers import setup

print(sys.path)
req = REQ()
current_time = "sfsgs"
class DogTests(unittest.TestCase):


    # testing for return list and bulldog': ['boston', 'french'] exist in list. Can also be split in 2
    def test_breeds_list_all(self):
        dog_list = req.get(setup.base_url+setup.listBreeds)
        response_body = dog_list[1]
        response_code = dog_list[0]
        assert response_code == 200, "Invalid Response {} Expected 200".format(response_code)
        assert response_body['message']['bulldog'][0] == setup.bulldoglist[0] and \
            response_body['message']['bulldog'][0] == setup.bulldoglist[0], 'Cannot find Buldog in lit'

    # checking for response code 200 and success status
    def test_random_image(self):
        random_image = req.get(setup.base_url+setup.random_image)
        response_body = random_image[1]
        response_code = random_image[0]
        assert response_code == 200, "Invalid Response {} Expected 200".format(response_code)
        assert response_body['status'] == setup.success['status']

    # makes a a call to the all list api and vaidates that all existing bredds have and image
    #this may take may tke a whle to execute snce I am going through the whole list
    def test_breeds_images(self):
        dog_list = req.get(setup.base_url+setup.listBreeds)
        response_body = dog_list[1]
        response_code = dog_list[0]
        assert response_code == 200, "Invalid Response {} Expected 200".format(response_code)
        for i in response_body['message']:
            endpoint = str(i) + setup.byBreed
            image_list = req.get(setup.base_single_breed+endpoint)
            response_body = image_list[1]
            response_code = image_list[0]
            assert response_code == 200, "Invalid Response {} Expected 200".format(response_code)
            assert response_body['message'] != None, "No images for breed {} ".format(i)

    #Will verify bulldog breed returns the correct list of sub breeds from breed api
    def test_breed_list(self):
        sub_breed_list = req.get(setup.base_url + setup.listBreeds)
        response_body = sub_breed_list[1]
        response_code = sub_breed_list[0]
        assert response_code == 200, "Invalid Response {} Expected 200".format(response_code)
        assert response_body['message']['bulldog'][0] == setup.bulldoglist[0] and \
               response_body['message']['bulldog'][0] == setup.bulldoglist[0], 'Cannot find Buldog in lit'

    # Will test an image is return from the random breed list
    def test_random_picture_list(self):
        dog_list = req.get(setup.base_url + setup.listBreeds)
        response_body = dog_list[1]
        response_code = dog_list[0]
        assert response_code == 200, "Invalid Response {} Expected 200".format(response_code)
        for i in response_body['message']:
            endpoint = str(i) + setup.random_images
            random_breed_list = req.get(setup.base_single_breed + endpoint)
            response_body = random_breed_list[1]
            response_code = random_breed_list[0]
            assert response_code == 200, "Invalid Response {} Expected 200".format(response_code)
            assert response_body['message'] != None, "No images for breed {} ".format(i)

    # The Following to negative test cases can be applied for all endpoints
    # Negative test for malformed endpoint
    def test_neg_breeds_list_all(self):
        try:
            dog_list = req.get(setup.base_url+ setup.listBreeds+"l")
            response_body = dog_list[1]
            response_code = dog_list[0]
            assert response_code == 404, "Invalid Response {} Expected 200".format(response_code)
            assert response_body == setup.error_string, "Invalid Error body return".format(response_body)
        except ValueError:
            print("malforform endpoint encoutered")

    #Negative test for invalid breed
    def test_neg_breeds_lists_all(self):
        endpoint = setup.invalid_breed + setup.random_images
        random_breed_list = req.get(setup.base_single_breed + endpoint)
        response_body = random_breed_list[1]
        response_code = random_breed_list[0]
        assert response_code == 404, "Invalid Response {} Expected 200".format(response_code)
        assert response_body['message'] == "Breed not found"








