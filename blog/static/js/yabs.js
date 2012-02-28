var Post = function () {
    this.title = ko.observable();
    this.content = ko.observable();
    this.author = ko.observable();
    this.tags = ko.observable();
    //this.date = new Date()
}

var PostViewModel = function () {
    // Data
    var self = this;
    self.posts = ko.observableArray([new Post()]);
    self.newPost = ko.observable(new Post());

    // Load data from server
    $.getJSON("/post/.json", function(data) {
        $.each(data, function(i, item){            
            $('div.post-container').append('<p>' + ko.toJSON(item) + '</p>');
        });
    });

    // Save data to server
    self.savePost = function () {
        alert(ko.toJSON(self.newPost()));
        $.ajax("/post/new", {
            data: ko.toJSON(self.newPost()),
            type: "post", contentType: "application/html",
            success: function(result) { alert(result) }
        });
    };
}

ko.applyBindings(new PostViewModel());
