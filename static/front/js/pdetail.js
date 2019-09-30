$(function () {
    var ue = UE.getEditor("editor", {
        'serverUrl': '/ueditor/upload/',
        "toolbars": [
            //定制按钮
            [
                'undo', //撤销
                'redo', //重做
                'bold', //加粗
                'italic', //斜体
                'source', //源代码
                'blockquote', //引用
                'selectall', //全选
                'insertcode', //代码语言
                'fontfamily', //字体
                'fontsize', //字号
                'simpleupload', //单图上传
                'emotion' //表情
            ]
        ]
    });
    window.ue = ue;
});

$(function () {
    $('#comment-btn').click(function (event) {
        //添加评论
        event.preventDefault();
        var flag = $('#login-tag').attr('data-is-login');
        //标志用户是否登录
        if (!flag) {
            window.location = '/login/';
        } else {
            var content = window.ue.getContent();//获取内容
            var post_id = $("#post-content").attr('data-id');

            zlajax.post({
                'url': '/add_comment/',
                'data': {
                    'content': content,
                    'post_id': post_id
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