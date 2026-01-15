var app = angular.module("rentkartApp", ["ngRoute"]);

app.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl: "partials/home.html",
        controller: "HomeController"
    })
    .when("/login", {
        templateUrl: "partials/login.html",
        controller: "LoginController"
    })
    .when("/products/:categoryId", {
    templateUrl: "partials/products.html",
    controller: "ProductController"
})
    .when("/subscriptions", {
        templateUrl: "partials/subscriptions.html",
        controller: "SubscriptionController"
    })
    .otherwise({
        redirectTo: "/"
    });
});
