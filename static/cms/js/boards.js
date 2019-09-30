$(function () {
    $("#add-board-btn").click(function (event) {
        event.preventDefault();
        mbalert.alertOneInput({
            'text': '请输入板块名称！',
            'placeholder': '板块名称',
            'confirmCallback': function (inputValue) {
                zlajax.post({
                    'url': '/cms/add_board/',
                    'data': {
                        'name': inputValue
                    },
                    'success': function (data) {
                        if (data['code'] == 200) {
                            window.location.reload();
                        } else {
                            mbalert.alertInfo(data['message']);
                        }
                    }
                });
            }
        });
    });
});

$(function () {
    $(".edit-board-btn").click(function () {
        var self = $(this);
        var tr = self.parent().parent();
        var name = tr.attr('data-name');
        var board_id = tr.attr("data-id");

        mbalert.alertOneInput({
            'text': '请输入新的板块名称！',
            'placeholder': name,
            'confirmCallback': function (inputValue) {
                zlajax.post({
                    'url': '/cms/update_board/',
                    'data': {
                        'board_id': board_id,
                        'name': inputValue
                    },
                    'success': function (data) {
                        if (data['code'] == 200) {
                            window.location.reload();
                        } else {
                            mbalert.alertInfo(data['message']);
                        }
                    }
                });
            }
        });
    });
});


$(function () {
    $(".delete-board-btn").click(function (event) {
        var self = $(this);
        var tr = self.parent().parent();
        var board_id = tr.attr("data-id");
        console.log(board_id);
        mbalert.alertConfirm({
            "msg": "您确定要删除这个板块吗？",
            'confirmCallback': function () {
                zlajax.post({
                    'url': '/cms/delete_board/',
                    'data': {
                        'board_id': board_id
                    },
                    'success': function (data) {
                        if (data['code'] == 200) {
                            window.location.reload();
                        } else {
                            mbalert.alertInfo(data['message']);
                        }
                    }
                })
            }
        });
    });
});