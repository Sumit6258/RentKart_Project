app.factory("ApiService", function($http) {

    var BASE_URL = "http://127.0.0.1:8000/api";

    return {

        sendOtp: function(phone) {
            return $http.post(BASE_URL + "/accounts/send-otp/", { phone: phone });
        },

        verifyOtp: function(data) {
            return $http.post(BASE_URL + "/accounts/verify-otp/", data);
        },

        getCategories: function() {
            return $http.get(BASE_URL + "/catalog/categories/");
        },

        getProducts: function() {
            return $http.get(BASE_URL + "/catalog/products/");
        },

        createSubscription: function(data) {
            return $http.post(BASE_URL + "/subscriptions/subscriptions/", data);
        },

        getSubscriptions: function(phone) {
            return $http.get(BASE_URL + "/subscriptions/subscriptions/?phone=" + phone);
        }
    };
});
