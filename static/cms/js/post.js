$(function () {
    $(".edit-post-btn").click(function () {
        var self = $(this);
        var tr = self.parent().parent();
        var post_id = tr.attr('data-id');
        var highlight = parseInt(tr.attr("data-highlight"));        //parseInt解析成int类型

        var url = '';
        if (highlight) {
            url = "/cms/remove_highlight/";
        } else {
            url = "/cms/add_highlight/";
        }
        zlajax.post({
            'url': url,
            'data': {
                'post_id': post_id
            },
            'success': function (data) {
                if (data['code'] == 200) {
                    mbalert.alertSuccessToast('操作成功！');
                    setTimeout(function () {
                        window.location.reload();
                    }, 500);

                } else {
                    mbalert.alertInfo(data['message']);
                }
            }
        });
    });
});

