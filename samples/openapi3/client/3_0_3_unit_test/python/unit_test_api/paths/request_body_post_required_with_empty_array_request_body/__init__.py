# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from unit_test_api.paths.request_body_post_required_with_empty_array_request_body import Api

from unit_test_api.paths import PathValues

path = PathValues.REQUEST_BODY_POST_REQUIRED_WITH_EMPTY_ARRAY_REQUEST_BODY