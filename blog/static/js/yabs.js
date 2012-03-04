var Post = function () {
    this.title = ko.observable();
    this.content = ko.observable();
    this.author = ko.observable();
    this.tags = ko.observable();
}

var viewModel = ko.mapping.fromJS(data);

var newPost = function() { this.test = ko.observable(new Post());}

var savePost = function () {
    alert(ko.toJSON(newPost().test));
    $.ajax("/post/new", {
        data: ko.toJSON(newPost), dataType: "json",
        type: "post", contentType: "application/json",
        success: function(result) { alert(result) }
     });
};

var data = $.getJSON("/post/.json", function(data) {
    ko.mapping.fromJS(data, viewModel);
});

$(document).ready(function() {
    ko.applyBindings(viewModel);
});
