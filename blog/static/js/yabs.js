var Post = function (title, content, author, tags, date, _id) {
    this.title = ko.observable(title);
    this.content = ko.observable(content);
    this.author = ko.observable(author);
    this.tags = ko.observable(tags);
    this.date = date;
    this._id = _id;
}

var mapping = {
    create: function(options) {
        return new Post(options.data.title, options.data.content, options.data.author, 
                options.data.tags, options.data.date, options.data._id.$oid);
    }
};

var initialData = ko.mapping.fromJS(data)

var data = $.getJSON("/post/.json", function(data) {
        ko.mapping.fromJS(data, initialData);
});

var viewModel = {
    post: ko.mapping.fromJS(initialData, mapping)
};

//var newPost = function() { this.test = ko.observable(new Post());}

/*var savePost = function () {
    alert(ko.toJSON(newPost().test));
    $.ajax("/post/new", {
        data: ko.toJSON(newPost), dataType: "json",
        type: "post", contentType: "application/json",
        success: function(result) { alert(result) }
     });
};*/

$(document).ready(function() {
    ko.applyBindings(viewModel);
});
