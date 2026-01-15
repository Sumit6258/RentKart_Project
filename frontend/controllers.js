app.controller("HomeController", function($scope) {
    $scope.message = "Rent Appliances Easily with Rentkart";
});


app.controller("LoginController", function($scope, ApiService, $location) {

    $scope.sendOtp = function() {
        ApiService.sendOtp($scope.phone).then(() => {
            $scope.otpSent = true;
        });
    };

    $scope.verifyOtp = function() {
        ApiService.verifyOtp({
            phone: $scope.phone,
            otp: $scope.otp
        }).then((res) => {
            localStorage.setItem("customer_id", res.data.customer_id);
            localStorage.setItem("phone", res.data.phone);

            // 🔥 REAL FEEL
            $location.path("/");
        });
    };
});




app.controller("ProductController", function($scope, ApiService, $routeParams) {

    var categoryId = $routeParams.categoryId;

    ApiService.getProducts().then(res => {
        $scope.products = res.data.filter(p => p.category === parseInt(categoryId));
    });
});



app.controller("SubscriptionController", function($scope, ApiService) {

    var phone = localStorage.getItem("phone");

    ApiService.getSubscriptions(phone).then((res) => {
        $scope.subscriptions = res.data;
    });
});

app.controller("NavController", function($scope, ApiService, $location) {

    $scope.isLoggedIn = !!localStorage.getItem("customer_id");

    if ($scope.isLoggedIn) {
        ApiService.getCategories().then(res => {
            $scope.categories = res.data;
        });
    }

    $scope.logout = function() {
        localStorage.clear();
        $scope.isLoggedIn = false;
        $location.path("/login");
    };
});

