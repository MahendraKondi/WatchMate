from rest_framework.throttling import UserRateThrottle

class ReviewCreateThrottle(UserRateThrottle):
    scope = 'reviewcreate'


class ReviewlistThrottle(UserRateThrottle):
    scope = 'reviewlist'


class ReviewdetailThrottle(UserRateThrottle):
    scope = 'reviewdetail'